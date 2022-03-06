from agent import Agent
from map import Map
from paths import Paths
from color import *

import pygame
from pygame import gfxdraw
import numpy as np


class Visualizer(object):
  def __init__(self, map_file, paths_file, grid_size=30, fps=30, show_start=1):
    self.Map = Map(map_file)
    self.Paths = Paths(paths_file)
    self.agent_num = self.Paths.paths_num
    self.colors = []
    k_contrast_color(self.agent_num, self.colors)
    self.Agents = []
    for i in range(self.agent_num):
      self.Agents.append(Agent(i, 
                              self.colors[i], 
                              self.Paths.paths[i]))
    self.arrival = np.zeros((self.agent_num, 1), dtype=np.bool)
    self.grid_size = grid_size

    self.fps = fps
    self.show_start = show_start
    self.time = 0
    self.finish = 0
    self.reset = 0
    self.quit = 0


  def display(self):
    grid_size = self.grid_size
    grid_len = self.Map.len
    grid_wid = self.Map.wid
    win_len = grid_len*grid_size
    win_wid = grid_wid*grid_size
    half_size = grid_size//2
    radius = round(half_size*0.75)
    font_size = round(radius*1.3)

    pygame.init()
    pygame.font.init()
    self.font = pygame.font.Font("./font_yaheibold.ttf", font_size)
    screen = pygame.display.set_mode((win_len, win_wid))
    clock = pygame.time.Clock()
    
    grids = [pygame.Surface((grid_size, grid_size), 
                        pygame.SRCALPHA).convert_alpha() \
                        for _ in range(grid_len*grid_wid)]
    agents = [pygame.Surface((grid_size, grid_size), 
                        pygame.SRCALPHA).convert_alpha() \
                        for _ in range(self.agent_num)]
    agents_b = [pygame.Surface((grid_size, grid_size), 
                        pygame.SRCALPHA).convert_alpha() \
                        for _ in range(self.agent_num)]

    map_back = pygame.surface.Surface((win_len, win_wid), 
                                      pygame.SRCALPHA, 32)
    map_back = map_back.convert_alpha()
    agent_back = pygame.surface.Surface((win_len, win_wid), 
                                      pygame.SRCALPHA, 32)
    agent_back = agent_back.convert_alpha()

    map_back.fill((0,0,0,0)) # render map
    for i in range(grid_len):
      for j in range(grid_wid):
        if self.Map.map[j][i] == 0:
          grid_color = (225, 225, 225)
        elif self.Map.map[j][i] == 1:
          grid_color = (128, 128, 128)
        else:
          grid_color = (0, 0, 0)
        grids[j*grid_len+i].fill(pygame.Color(grid_color))
        map_back.blit(grids[j*grid_len+i], 
                            ((i)*grid_size, 
                              (j)*grid_size))
    
    for i in range(self.agent_num): # render starts and ends
      start_x = self.Agents[i].path[0][1] * grid_size
      start_y = self.Agents[i].path[0][0] * grid_size
      end_x = self.Agents[i].path[-1][1] * grid_size
      end_y = self.Agents[i].path[-1][0] * grid_size

      target_color = pygame.Color(0,0,0)
      target_color.hsva = self.colors[i]
      
      if self.show_start:
        gfxdraw.box(map_back, 
                    pygame.Rect(start_x-radius+half_size,
                                start_y-radius+half_size, 
                                2*radius, 
                                2*radius), 
                    target_color)
        gfxdraw.rectangle(map_back, 
                          pygame.Rect(start_x-radius+half_size,
                                      start_y-radius+half_size, 
                                      2*(radius), 
                                      2*(radius)), 
                          (0,0,0))
      gfxdraw.filled_trigon(map_back, 
                            end_x+half_size, end_y+half_size-radius, 
                            end_x+half_size-round(radius/2*1.7321), end_y+half_size+radius//2, 
                            end_x+half_size+round(radius/2*1.7321), end_y+half_size+radius//2, 
                            target_color)
      gfxdraw.aatrigon(map_back, 
                        end_x+half_size, end_y+half_size-radius, 
                        end_x+half_size-round(radius/2*1.7321), end_y+half_size+radius//2, 
                        end_x+half_size+round(radius/2*1.7321), end_y+half_size+radius//2, 
                        (0,0,0))
      # gfxdraw.rectangle(starts, 
      #                   pygame.Rect(left, top, width, height), 
      #                   agent_color)
      # gfxdraw.box(starts, 
      #             pygame.Rect(left, top, width, height), 
      #             agent_color)

    frame_count = 0
    while 1:
      clock.tick(self.fps)

      if self.quit:
        break
        
      if self.finish: 
        if self.reset:
          self.reset()
      else:
        frame_count += 1
        if frame_count % self.fps == 0:
          self.time += 1

        agent_back.fill((0,0,0,0))
        for i in range(self.agent_num): # render agent
          agents[i].fill((0,0,0,0))

          agent_color = pygame.Color(0,0,0)
          agent_color.hsva = self.colors[i]

          cur_agent = self.Agents[i]
          if self.time < cur_agent.path_len-1: # not arrive
            grid_pos = cur_agent.path[self.time]
            grid_shift_x = cur_agent.path[self.time+1][1] - grid_pos[1]
            grid_shift_y = cur_agent.path[self.time+1][0] - grid_pos[0]
            pix_x = round(grid_pos[1]*grid_size+
                          grid_shift_x*(frame_count%self.fps)/self.fps*grid_size)
            pix_y = round(grid_pos[0]*grid_size+
                          grid_shift_y*(frame_count%self.fps)/self.fps*grid_size)
          else: # arrive
            if not self.arrival[i]:
              print('agent', i, 'arrive at end point')
              self.arrival[i] = 1
            
            if len(np.argwhere(1-self.arrival))==0:
              print('finish')
              self.finish = 1
            grid_pos = cur_agent.path[cur_agent.path_len-1]
            pix_x = grid_pos[1] * grid_size
            pix_y = grid_pos[0] * grid_size

          gfxdraw.aacircle(agents_b[i], 
                            half_size, 
                            half_size, 
                            radius, 
                            (0,0,0))
          gfxdraw.filled_circle(agents[i], 
                                half_size, 
                                half_size, 
                                radius, 
                                agent_color)
          info_color = pygame.Color(255-agent_color.r,
                                    255-agent_color.g,
                                    255-agent_color.b)
          info = self.font.render(#'{}' # number
                                  #.format(i),
                                  '999',
                                  True, 
                                  info_color)
          info_len = len(str(i))

          agent_back.blit(agents[i], (pix_x,pix_y))
          agent_back.blit(agents_b[i], (pix_x,pix_y))
          agent_back.blit(info, (round(pix_x+radius-font_size/3*info_len/2.0),
                                  round(pix_y+radius-font_size/3)))

        screen.blit(map_back, (0,0))
        screen.blit(agent_back, (0,0))
        pygame.display.update()

      pygame.display.set_caption("MAPF Visualizer    fps: " + 
                                "{:2.2f}".format(clock.get_fps()) +
                                "    time step: " + 
                                "{:2.2f}".format(self.time+(frame_count%self.fps)/self.fps)) 
                                # str(self.clock.get_fps())

      for event in pygame.event.get(): # keyboard control
        if event.type == pygame.QUIT:
          self.quit = 1
    
    pygame.quit()


if __name__ == '__main__':
  vis = Visualizer('random-32-32-20.map', 'paths.txt', show_start=0)
  vis.display()