class Agent(object):
  def __init__(self, number, color, path, k_robust, size_l, size_w):
    self.number = number
    self.color = color
    self.path = path
    self.path_len = len(path)
    self.start = path[0]
    self.end = path[-1]
    self.k_robust = k_robust
    self.size_l = size_l
    self.size_w = size_w
    self.arrival = 0