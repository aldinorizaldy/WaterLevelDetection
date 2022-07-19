import numpy as np
import cv2

frame = cv2.imread("adnan_rotate.png")
#slc = frame[250:500,0:1800] # pilih hanya di palm dan buang tepi
slc = frame[0:1800,500:750] # pilih hanya di palm dan buang tepi

test_line = 1310
# found that the top 300 cm is 400 px; bottom at 170 cm is 1310 px
# Then we need to calculate the relationship between those data
# 

cv2.line(frame,pt1=(0,test_line),pt2=(1800,test_line),color=(0,0,255), thickness=4)
cv2.imwrite("calibrate_water_level.png",frame)