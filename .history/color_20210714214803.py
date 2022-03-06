import pygame
import math


def k_contrast_color(k_color):
  # hue: 0-360, min_step: 5(72)
  # sat: 0.3-0.8, min_step: 0.1(6)
  # int: 0.5-1.0, min_step: 0.1(6)
  # max_color = 72*6*6 = 2592

  H = 360
  S = 1
  I = 1
  RGB_list = []

  if k_color <= 2592:
    if k_color <= 432:
      if k_color <= 72: # 1-72
        S = 1
        I = 1
        H_step = 360 // k_color
        for i in range(k_color):
          Hi = i
          tmp_H = Hi * H_step 
          RGB_list.append(HSI2RGB(tmp_H, S, I))
      else: # 73-432
        I = 1
        H_step = 5
        S_num = math.ceil(k_color / 72)
        S_step = 0.5 / (S_num-1)
        for i in range(k_color):
          Hi = i % 72
          tmp_H = Hi * H_step
          Si = math.floor(i / 72)
          tmp_S = 0.8 - Si * S_step
          RGB_list.append(HSI2RGB(tmp_H, tmp_S, I))

    else: # 433-2592
        S_step = 0.1
        H_step = 5
        I_num = math.ceil(k_color / 432)
        I_step = 0.5 / (I_num-1)
        for i in range(k_color):
          Hi = i % 72
          tmp_H = Hi * H_step
          Si = (i/72) % 6
          tmp_S = 0.8 - Si * S_step
          Ii = math.floor(i / 432)
          tmp_I = 1.0 - Ii * I_step
          RGB_list.append(HSI2RGB(tmp_H, tmp_S, tmp_I))
    
  else : # >2592
    print("FAIL: NUM OF COLOR IS TOO LARGE.")

  return RGB_list


def HSI2RGB(H, S ,I):
  # print('H:', H, ', S:', S, ', I:', I)
  R = 0
  G = 0
  B = 0
  if S < 1e-6:
    R = I
    G = I
    B = I
  else:
    if H >= 0 and H < 120:
      B = I * (1 - S)
      R = I * (1 + (S * math.cos(H*math.pi/180)) / math.cos((60 - H)*math.pi/180))
      G = 3 * I - (R + B)
    elif H >= 120 and H < 240:
      H = H - 120
      R = I * (1 - S)
      G = I * (1 + (S * math.cos(H*math.pi/180)) / math.cos((60 - H)*math.pi/180))
      B = 3 * I - (R + G)
    elif H >= 240 and H < 360:
      H = H - 240
      G = I * (1 - S)
      B = I * (1 + (S * math.cos(H*math.pi/180)) / math.cos((60 - H)*math.pi/180))
      R = 3 * I - (G + B)
    else:
      print("ERROR: H not in [0, 360]")
      return
  # print('R:', R, ', G:', G, ', B:', B)

  if R >= 1.0:
    R = 1.0
  if G >= 1.0:
    G = 1.0
  if B >= 1.0:
    B = 1.0

  return [round(R*255), round(G*255), round(B*255)]


if __name__ == '__main__':

  pygame.init()

  grid_len = 72
  grid_wid = 50 
  grid_size = 10
  win_len = grid_len*grid_size
  win_wid = grid_wid*grid_size

  screen = pygame.display.set_mode((win_len, win_wid))
  pygame.display.set_caption('k contrast color')

  grids = [pygame.Surface((grid_size, grid_size), 
                          pygame.SRCALPHA).convert_alpha() \
                          for _ in range(grid_len*grid_wid)]
  map_back = pygame.surface.Surface((win_len, win_wid), 
                                    pygame.SRCALPHA, 32)
  map_back = map_back.convert_alpha()

  colors = k_contrast_color(grid_len*grid_wid)
  print(colors)
  map_back.fill((0,0,0,0))
  while 1:
    for i in range(grid_len):
      for j in range(grid_wid):
        color = colors[j*grid_len+i]
        # print(color)
        grids[j*grid_len+i].fill(pygame.Color(color))
        map_back.blit(grids[j*grid_len+i], 
                            ((i)*grid_size, 
                              (j)*grid_size))
    screen.blit(map_back, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()