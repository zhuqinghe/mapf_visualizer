from agent import Agent
from color import *


class Visualizer(object):
  def __init__(self, map_file, path_file):
    pass

def readPaths(paths_file, paths):
  lines = []
  paths = []
  with open(paths_file, 'r') as fr:
    for i in range(10000):
      line_data = fr.readline()
      print('i', i)
      if line_data.strip() == "": # endline
        break
      else:
        path = line_data.strip(': ')
        lines.append(line_data)
    path_num = len(lines)
    

  for li in range(path_num):
    if lines[li].strip():
      tmp_line = lines[li].strip()
      print(tmp_line)
      pointStr = tmp_line.strip('->')
      # print(pointStr)
    else:
      print('[ERROR]: PATH', li , 'IS EMPTY')


def display(map, agents):
  pass


def main():
  map = []
  agents = []
  paths = []
  colors = []

  paths_file = ""
  
  readPaths(paths_file, paths)
  path_num = len(paths)
  k_contrast_color(path_num, colors)

  for i in range(path_num):
    agents.append(Agent(i, colors[i], paths[i]))

  display(map, agents)


if __name__ == '__main__':
  paths = []
  readPaths('paths.txt', paths)