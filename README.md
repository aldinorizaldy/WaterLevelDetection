# WaterLevelDetection
A simple computer vision technique for water level detection

![hasil_detection_2](https://user-images.githubusercontent.com/52752546/179653909-282c199c-d96c-4a8a-aa43-b46745e3d089.png)

Steps:
1. Calibration
   In cmd / terminal, run: python calibrate_water_level.py 
   This step is to estimate the top and bottom of the measurement. Those values will be used to calculate the water level from the detection.
2. Detection
   In cmd / terminal, run: python water_level_detection.py your_video_file.
   
This detection works by simply performing Canny Edge Detection and find lines using Houghlines. Then it assumes that the lowest line is the water level since there is no line below the water level. 

Result of all detected lines only on the area of interest (between red lines):
![hasil_detection_2](https://user-images.githubusercontent.com/52752546/179654705-1640a55a-14b6-41ff-9132-729e4732a5d1.png)


Examples for the calibration:
![calibrate_water_level_top](https://user-images.githubusercontent.com/52752546/179654009-aeaa7a70-0274-438b-addb-378b8960c6c7.png)
![calibrate_water_level_bottom](https://user-images.githubusercontent.com/52752546/179654019-10ca016d-b7ae-4ef1-bca9-dc756596b49c.png)
