# codes by: Aldino Rizaldy (2002)
# free to share

###########################################################################################
# WATER LEVEL DETECTION USING COMPUTER VISION

# Install dependencies:
# - numpy
# - opencv

# How to use
# On command prompt / terminal, Run: python water_level_detection.py your_input_video.mp4
# Result on Water_Level_Detection_Result.mp4

import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser(description="Water Level Detection")
parser.add_argument("input_video", type=str,
                    help="The path of the input video.")
parser.add_argument("--save_video", type=lambda x: (str(x).lower() == 'true'), default=True,
                    help="Whether to save the video detection results.")
args = parser.parse_args()

vid = cv2.VideoCapture(args.input_video)
video_frame_cnt = int(vid.get(7))
video_width = int(vid.get(3))
video_height = int(vid.get(4))
video_fps = int(vid.get(5))

if args.save_video:
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    videoWriter = cv2.VideoWriter('Water_Level_Detection_Result.mp4', fourcc, video_fps, (video_width, video_height))

for i in range(video_frame_cnt): # dikurangi 10 karena kalo sampe akhir ada error message
    ret, frame = vid.read()

    
    slc = frame[0:1800,500:750] # CHANGE ACCORDING TO THE DATA !! Here we only take that specific area for the detection 
    gray_slc = cv2.cvtColor(slc, cv2.COLOR_BGR2GRAY)

    # Run Canny Edge Detector
    edges = cv2.Canny(gray_slc, 50, 90) # Change if needed
    
    # Change following parameters if needed
    rho = 1
    theta = np.pi / 180
    threshold = 15
    min_line_length = 50
    max_line_gap = 20

    # Hough Lines
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    #for line in lines:
    #    for x1,y1,x2,y2 in line:
    #        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),5) # to plot all lines

    water_level = int((max(lines[:,0,1]) + max(lines[:,0,3])) / 2) # mencari kedua posisi koordinat Y pada garis terjauh 
    water_level = water_level - 150 # untuk menaikkan dari garis deteksi yang cenderung tenggelam (TERGANTUNG DATA !!)
    cv2.line(frame,pt1=(250,water_level),pt2=(1000,water_level),color=(0,0,255), thickness=4) # CHANGE ACCORDING TO THE DATA !!
    
    # CHANGE ACCORDING TO THE CALIBRATION FROM MANUAL MEASUREMENT !!
    # Following values are measured from calibration (calibrate_water_level.py)
    top_cal_px = 400
    top_cal_cm = 300
    bottom_cal_px = 1310
    bottom_cal_cm = 170
    str_WL = ((water_level-top_cal_px)/(bottom_cal_px-top_cal_px)) * (bottom_cal_cm-top_cal_cm) + top_cal_cm
    str_WL = str(int(str_WL))
    TinggiAir = "Water Level = "
    cm = " cm"
    str_all = TinggiAir + str_WL + cm
    cv2.putText(frame,str_all, (70,1150), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(255,255,255),thickness=2)
    cv2.putText(frame,"Computer Vision Detection", (70,1100), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(255,255,255),thickness=2)

    #cv2.imshow("hasil",frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    if args.save_video:
        videoWriter.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break        
vid.release()
if args.save_video:
        videoWriter.release()