from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera=PiCamera()
camera.resolution=(720, 640)
camera.framerate=32
rawCapture=PiRGBArray(camera, size=(720, 640))

time.sleep(5)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  image=frame.array
  cv2.imshow("Frame", image)
  key=cv2.waitKey(1) & 0xFF
  rawCapture.truncate(0)

  if key==ord("q"):
      break