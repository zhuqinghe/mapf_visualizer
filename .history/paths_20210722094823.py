class PathsLoader(object):
  def __init__(self, path_file):
    self.paths, self.paths_len = self.readPaths(path_file)
    self.paths_num = len(self.paths_len)

  def readPaths(self, paths_file):
    lines = []
    paths = []
    paths_len = []
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
        paths_len.append(len(tmp_path))
      else:
        print('[ERROR]: PATH', li , 'IS EMPTY')
    # print('paths:', paths, len(paths))

    return paths, paths_len

  def displayPaths(self):
    print('========paths begin========')
    for i in range(self.paths_num):
      print('Path-{} ({}):'.format(i,self.paths_len[i]), self.paths[i])
    print('========paths end========')

if __name__ == '__main__':
  paths = Paths('paths.txt')
  paths.displayPaths()