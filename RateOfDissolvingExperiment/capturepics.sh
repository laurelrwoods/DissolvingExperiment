#!/bin/bash

cam_index=0
num_cams=2

while [ $cam_index -lt $num_cams ]
do
	if [ $cam_index -eq 0 ]
	then
		path=Pictures/Beaker1/TopCam/
	elif [ $cam_index -eq 1 ]
	then
		path=Pictures/Beaker1/SideCam/
	elif [ $cam_index -eq 2 ]
	then
		path=Pictures/Beaker2/TopCam/
	elif [ $cam_index -eq 3 ]
	then
		path=Pictures/Beaker2/SideCam/
	elif [ $cam_index -eq 4 ]
	then
		path=Pictures/Beaker3/TopCam/
	elif [ $cam_index -eq 5 ]
	then
		path=Pictures/Beaker3/SideCam/
	elif [ $cam_index -eq 6 ]
	then
		path=Pictures/Beaker4/TopCam/
	elif [ $cam_index -eq 7 ]
	then
		path=Pictures/Beaker4/SideCam/
	elif [ $cam_index -eq 8 ]
	then
		path=Pictures/Beaker5/TopCam/
	elif [ $cam_index -eq 9 ]
	then
		path=Pictures/Beaker5/SideCam/
	fi
	
	filename=$(date +%y.%m.%d.%H.%M.%S)
	fswebcam -d /dev/video$cam_index -r 2000x2000 /home/pi/Documents/MaterialDecay/$path$filename.jpg

	wget -q --tries=10 --timeout=20 --spider http://google.com
	if [ $? -eq 0 ]
	then
		/home/pi/.local/bin/aws s3 mv /home/pi/Documents/MaterialDecay/$path$filename.jpg s3://ice911/Data/"Material Decay Experiment, 6-19-2017"/$path

	fi
	((cam_index++))


done


