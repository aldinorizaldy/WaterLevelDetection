# WaterLevelDetection
A simple computer vision technique for water level detection

![hasil_detection_1](https://user-images.githubusercontent.com/52752546/179656137-965726bf-f36e-41e8-99cd-aad6c5925b56.png)

Steps:
1. Calibration
   In cmd / terminal, run: python calibrate_water_level.py 
   This step is to estimate the top and bottom of the measurement. Those values will be used to calculate the water level from the detection.
2. Detection
   In cmd / terminal, run: python water_level_detection.py your_video_file.
   
This detection works by simply performing Canny Edge Detection and find lines using Houghlines. Then it assumes that the lowest line is the water level since there is no line below the water level. 


Result of all detected lines only on the area of interest (between red lines):


![hasil_detection_2_small](https://user-images.githubusercontent.com/52752546/179655890-422f6992-6f0c-4b19-8f28-948ed3c69ed1.png)


Examples for the calibration:
Top = 300 cm
Bottom = 170 cm

![calibrate_water_level_top](https://user-images.githubusercontent.com/52752546/179655836-acd2bc96-00ed-48fc-b8a9-f68d0fdbd9eb.png)
![calibrate_water_level_bottom](https://user-images.githubusercontent.com/52752546/179655849-34066f13-6f70-41a6-8a8b-ff3461be5b77.png)
