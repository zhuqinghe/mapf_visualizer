import pygame
import math


def k_contrast_color(k_color, RGB_list, HSV_list):
  # hue       : 0-360, min_step: 5(72)
  # saturation: 0.4-0.8, min_step: 0.1(5)
  # intensive : 0.5, min_step: 0.1(6)
  # max_color = 72*6*6 = 2592

  H_min_step = 5
  H_max_num = 360 // H_min_step
  S_min_step = 0.1
  S_max_num = math.floor(0.4 / S_min_step) + 1
  I_min_step = 0.1
  I_max_num = math.floor(0.5 / I_min_step) + 1

  H = 360
  S = 1
  I = 1

  if k_color <= H_max_num*S_max_num*I_max_num:
    if k_color <= H_max_num*S_max_num:
      if k_color <= H_max_num: 
        S = 1
        I = 1
        H_step = 360 // k_color
        for i in range(k_color):
          Hi = i
          tmp_H = Hi * H_step 
          RGB_list.append(HSI2RGB(tmp_H, S, I))
          HSV_list.append(tmp_H, S, I)
      else: 
        I = 1
        H_step = H_min_step
        S_num = math.ceil(k_color / H_max_num)
        S_step = 0.5 / (S_num-1)
        for i in range(k_color):
          Hi = i % H_max_num
          tmp_H = Hi * H_step
          Si = math.floor(i / H_max_num)
          tmp_S = 0.8 - Si * S_step
          RGB_list.append(HSI2RGB(tmp_H, tmp_S, I))
          HSV_list.append(tmp_H, tmp_S, I)

    else: 
        S_step = 0.1
        H_step = H_min_step
        I_num = math.ceil(k_color / (H_max_num*S_max_num))
        I_step = 0.5 / (I_num-1)
        for i in range(k_color):
          Hi = i % H_max_num
          tmp_H = Hi * H_step
          Si = (i//H_max_num) % S_max_num
          tmp_S = 0.8 - Si * S_step
          Ii = math.floor(i / (H_max_num*S_max_num))
          tmp_I = 1.0 - Ii * I_step
          RGB_list.append(HSI2RGB(tmp_H, tmp_S, tmp_I))
          HSV_list.append(tmp_H, S, I)
    
  else : # >2592
    print("[ERROR]: NUM OF COLOR IS TOO LARGE.")

  return RGB_list, HSV_list


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
      print("[ERROR]: H not in [0, 360)")
      return
  # print('R:', R, ', G:', G, ', B:', B)


  return [round(R*255), round(G*255), round(B*255)]


if __name__ == '__main__':
  grid_len = 72
  grid_wid = 30 
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
  k_contrast_color(grid_len*grid_wid, rgb_colors, hsv_colors)
  # print('color len:', len(rgb_colors))
  # print(rgb_colors)
  map_back.fill((0,0,0))
  while 1:
    for i in range(grid_len):
      for j in range(grid_wid):
        color = pygame.Color(0,0,0,0)
        rgb_color = (rgb_colors[j*grid_len+i][0], 
                      rgb_colors[j*grid_len+i][1],
                      rgb_colors[j*grid_len+i][2],
                      255)
        hsv_color = (hsv_colors[j*grid_len+i][0], 
                      round(hsv_colors[j*grid_len+i][1]*100),
                      round(hsv_colors[j*grid_len+i][2]*100),
                      100)
        color.hsva = hsv_color
        # print(color)
        grids[j*grid_len+i].fill(pygame.Color.hsva)
        map_back.blit(grids[j*grid_len+i], 
                            ((i)*grid_size, 
                              (j)*grid_size))
    screen.blit(map_back, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()