class Map(object):
  def __init__(self, map_file):
    self.map = self.readMap(map_file)

  def readMap(self, map_file):
    with open(map_file, 'r')