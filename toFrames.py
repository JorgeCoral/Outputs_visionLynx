import cv2
import sys

videoPath  = sys.argv[1];
outputPath = sys.argv[2];

vidcap = cv2.VideoCapture(videoPath)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(outputPath + "%5d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
