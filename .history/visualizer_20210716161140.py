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
      if line_data.strip() == "": # endline
        break
      else:
        lines.append(line_data)

  for li,line_data in enumerate(lines):
    if line_data.split(': ')[1]:
      tmp_line = line_data.split(': ')[1].strip()
      tmp_points = tmp_line.split('->')
      tmp_path = []
      for pi in range(len(tmp_points)):
        if tmp_points[pi]:
          tmp_path.append(eval(tmp_points[pi]))
      paths.append(tmp_path)
    else:
      print('[ERROR]: PATH', li , 'IS EMPTY')
  print('paths:', paths, len(paths))


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