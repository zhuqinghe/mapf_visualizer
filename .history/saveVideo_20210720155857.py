  def saveVideo(width, height):
    self.save_video = 0
    frames = []
    imgs = glob.glob("./img/*.png")
    imgs = sorted(imgs, key=lambda name: int(name[6:-4]))

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter('/{}-agent_{}-setp.gif' \
                                  .format(self.agent_num, self.max_time), 
                                  fourcc, 
                                  self.fps, 
                                  (width,height))
    for img in imgs:
      frame = cv2.imread(img)
      videoWriter.write(frame)
    videoWriter.release()