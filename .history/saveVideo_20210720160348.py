import cv2
import glob

def saveVideo(width, height):
  imgs = glob.glob("./img/*.png")
  imgs = sorted(imgs, key=lambda name: int(name[6:-4]))

  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  videoWriter = cv2.VideoWriter('/{}-agent_{}-setp.mp4',
                                fourcc, 
                                30, 
                                (width,height))
  for img in imgs:
    frame = cv2.imread(img)
    videoWriter.write(frame)
  videoWriter.release()


if __name__ == "__main__":
  saveVideo(960,960)