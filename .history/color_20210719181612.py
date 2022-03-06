import pygame
import math


def k_contrast_color(k_color, HSV_list):
  # hue       : 0-360, min_step: 5(72)
  # saturation: 50-100, min_step: 10(5)
  # intensive : 50-100, min_step: 10(6)
  # max_color = 72*6*6 = 2592

  H_min_step = 8
  H_max_num = 360 // H_min_step
  S_min_step = 10
  S_max_num = math.floor(50 / S_min_step) + 1
  I_min_step = 10
  I_max_num = math.floor(60 / I_min_step) + 1

  H = 360
  S = 100
  I = 100
  T = 100

  if k_color <= H_max_num*S_max_num*I_max_num:
    if k_color <= H_max_num*S_max_num:
      if k_color <= H_max_num: 
        S = 100
        I = 100
        H_step = 360 // k_color
        for i in range(k_color):
          Hi = i
          tmp_H = Hi * H_step 
          HSV_list.append((tmp_H, S, I, T))
      else: # >H_max_num
        I = 100
        H_step = H_min_step
        S_num = math.ceil(k_color / H_max_num)
        S_step = 60 / (S_num-1)
        for i in range(k_color):
          Hi = i % H_max_num
          tmp_H = Hi * H_step
          Si = math.floor(i / H_max_num)
          tmp_S = 100 - Si * S_step
          HSV_list.append((tmp_H, tmp_S, I, T))

    else: # >H_max_num*S_max_num
        S_step = 10
        H_step = H_min_step
        I_num = math.ceil(k_color / (H_max_num*S_max_num))
        I_step = 60 / (I_num-1)
        for i in range(k_color):
          Hi = i % H_max_num
          tmp_H = Hi * H_step
          Si = (i//H_max_num) % S_max_num
          tmp_S = 100 - Si * S_step
          Ii = math.floor(i / (H_max_num*S_max_num))
          tmp_I = 100 - Ii * I_step
          HSV_list.append((tmp_H, tmp_S, tmp_I, T))
    
  else : # >H_max_num*S_max_num*I_max_num
    print("[ERROR]: NUM OF COLOR IS TOO LARGE.")

  return HSV_list


if __name__ == '__main__':
  grid_len = 45
  grid_wid = 49 
  grid_size = 10
  win_len = grid_len*grid_size
  win_wid = grid_wid*grid_size

  pygame.init()
  screen = pygame.display.set_mode((win_len, win_wid))
  pygame.display.set_caption('k contrast color')

  grids = [pygame.Surface((grid_size, grid_size), 
                          pygame.SRCALPHA).convert_alpha() \
                          for _ in range(grid_len*grid_wid)]
  map_back = pygame.surface.Surface((win_len, win_wid), 
                                    pygame.SRCALPHA, 32)
  map_back = map_back.convert_alpha()

  rgb_colors = []
  hsv_colors = []
  k_contrast_color(grid_len*grid_wid, hsv_colors)
  # print('color len:', len(rgb_colors))
  # print(rgb_colors)
  map_back.fill((0,0,0))
  while 1:
    for i in range(grid_len):
      for j in range(grid_wid):
        color = pygame.Color(0,0,0,0)
        color.hsva = hsv_colors[j*grid_len+i]
        # print(color)
        grids[j*grid_len+i].fill(color)
        map_back.blit(grids[j*grid_len+i], 
                            ((i)*grid_size, 
                              (j)*grid_size))
    screen.blit(map_back, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()