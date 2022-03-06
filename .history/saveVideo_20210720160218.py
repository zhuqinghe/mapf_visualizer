import cv2
import glob

def saveVideo(width, height):
  frames = []
  imgs = glob.glob("./img/*.png")
  imgs = sorted(imgs, key=lambda name: int(name[6:-4]))

  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  videoWriter = cv2.VideoWriter('/{}-agent_{}-setp.gif',
                                fourcc, 
                                30, 
                                (width,height))
  for img in imgs:
    frame = cv2.imread(img)
    videoWriter.write(frame)
  videoWriter.release()