from agent import Agent
from color import *

def readPaths(paths_file, paths):
  lines = []
  with open(paths_file, 'r') as fr:
    for i in range(10000):
      line_data = fr.readline()
      if line_data.strip() == "":
        break
      else:
        lines.append(line_data)
        
  for li,line in enumerate(lines):
          


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