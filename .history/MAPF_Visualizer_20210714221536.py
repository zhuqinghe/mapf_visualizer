from agent import Agent
from color import *

def readPaths(paths_file, paths):
  pass


def display(agents):
  pass


def main():
  time = 0
  agents = []
  paths = []
  colors = []

  paths_file = ""
  
  readPaths(paths_file, paths)
  path_num = len(paths)
  k_contrast_color(path_num, colors)

  for i in range(path_num):
    agents.append(Agent(i, colors[i], paths[i]))

  display()