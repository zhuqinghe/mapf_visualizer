import numpy as np

class Map(object):
  def __init__(self, map_file, empty='.', block='@'):
    self.empty = empty
    self.block = block
    # size
    self.map = self.readMap(map_file)

  def readMap(self, map_file):
    lines = []
    with open(map_file, 'r') as fr:
      for i in range(10): # read prefix info
        line_data = fr.readline()
        if line_data.strip():
          if line_data.find('map') != -1:
            print('[INFO]: MAP BEGIN IN LINE', i+1)
            break
        else:
          print('[ERROR]: MAP IS EMPTY')
          break


      for i in range(10000): # begin to read map
        line_data = fr.readline()
        if line_data.strip() == "":
          print('[INFO]: MAP READING COMPLETE')
          break
        else:
          print(line_data)
          lines.append(line_data)
    
    if lines:
      map_len = len(lines[0])-1
      map_wid = len(lines)
      print(map_len, map_wid)
      map = np.ones((map_wid, map_len), dtype=np.int)
    
    for li,line in enumerate(lines):
      for ci,char in enumerate(line):
        if char == '\n':
          continue
        elif char == self.empty:
          map[li][ci] = 0
        elif char == self.block:
          map[li][ci] = 1
        else:
          map[li][ci] = 2
    
    return map

  def displayMap(self):
    print('========map begin========')
    row = self.map.shape[0]
    for i in range(row):
      print(self.map[i])
    print('========map end========')


if __name__ == '__main__':
  map = Map('random-32-32-20.map')
  map.displayMap()
