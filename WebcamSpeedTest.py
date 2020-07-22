import time

import cv2
import v4l2
import arducam_mipicamera as arducam

import numpy as np
import math

# init system
print('Creating camera object...')
camera = arducam.mipi_camera()
print("Initalizing camera...")
camera.init_camera()
print("Setting mode...")
camera.set_mode(0)

camera.set_control(v4l2.V4L2_CID_EXPOSURE,1000)
camera.set_control(v4l2.V4L2_CID_GAIN,0)

fmt = camera.set_resolution(640,480)

# first one is slow for some reason...
# MyTime = time.time()
frame = camera.capture(encoding = 'raw')
# print('Raw Capture time: ' + str(time.time()-MyTime))

Iterations = 25
TimeSum = 0
for i in range(Iterations):
    MyTime = time.time()
    frame = camera.capture(encoding = 'jpeg')
    TimeSum += time.time()-MyTime
AvgTime = TimeSum/Iterations
print("Avg JPEG Capture Time: " + str(AvgTime))
# print("Sample JPEG length: " + str(len(frame.data)))
# print("JPEG data type: " + str(type(frame.data)))

TimeSum = 0
for i in range(Iterations):
    MyTime = time.time()
    frame = camera.capture(encoding = 'i420')
    TimeSum += time.time()-MyTime
AvgTime = TimeSum/Iterations
print("Avg i420 Capture Time: " + str(AvgTime))
# print("Sample i420 length: " + str(len(frame.data)))
# print("i420 data type: " + str(type(frame.data)))

TimeSum = 0
for i in range(Iterations):
    MyTime = time.time()
    frame = camera.capture(encoding = 'raw')
    TimeSum += time.time()-MyTime
AvgTime = TimeSum/Iterations
print("Avg raw Capture Time: " + str(AvgTime))
# print("Sample raw length: " + str(len(frame.data)))
# print("raw data type: " + str(type(frame.data)))

# Height = int(math.ceil(fmt[1]/16.0)*16)
# Width = int(math.ceil(fmt[0]/32.0)*32)
# Array = frame.as_array.reshape(Height,Width)
# print(Array.shape)

camera.close_camera()