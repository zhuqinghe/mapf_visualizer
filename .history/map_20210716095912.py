import numpy as np

class Map(object):
  def __init__(self, map_file):
    self.map = self.readMap(map_file)

  def readMap(self, map_file):
    lines = []
    with open(map_file, 'r') as fr:
      for i in range(5):
        line_data = fr.readline()
        if line_data.strip() == "":
          break
        else:
          if line_data.find('map'):

          lines.append(line_data)
    
    if lines:
      map_len = len(lines[0])
      map_wid = len(lines)
      map = np.ones((map_wid, map_len), dtype=np.int)
    
    for li,line in enumerate(lines):
      for 
    