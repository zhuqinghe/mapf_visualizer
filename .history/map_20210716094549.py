class Map(object):
  def __init__(self, map_file):
    self.map = self.readMap(map_file)

  def readMap(self, map_file):
    lines = []
    with open(map_file, 'r') as fr:
      for i in range(10000):
        line_data = fr.readline()
        if line_data.strip() == "":
          break
        else:
          lines.append(line_data)
    
    map_len = 
    map_wid = 