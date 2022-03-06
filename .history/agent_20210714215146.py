class Agent(object):
  def __init__(self, number, color, path, path_length, start, end, k_robust,size_l,size_w,arrival):
    self.number = number
    self.color = color
    self.path = path
    self.path_len = len(path)
    self.start = path[0]
    self.end = path[-1]