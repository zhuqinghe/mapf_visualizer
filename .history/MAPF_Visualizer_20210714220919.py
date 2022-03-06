from agent import Agent
from color import *

def readPaths(paths_file, paths):
  pass


def display(time):
  pass


def main():
  time = 0
  agents = []
  paths = []

  paths_file = ""
  
  readPaths(paths_file, paths)
  path_num = len(paths)
  for i in range(path_num):
    tmp_agent = Agent(i, color, path, k_robust, size_l, size_w)
    pass
