#!/bin/bash

wget -q --tries=10 --timeout=20 --spider http://google.com
if [ $? -eq 0 ]
then

	beakers=$(ls /home/pi/Documents/MaterialDecay/Pictures/)
	for b in $beakers
	do
		cameras=$(ls /home/pi/Documents/MaterialDecay/Pictures/$b/)
		for c in $cameras
		do
			files=$(ls /home/pi/Documents/MaterialDecay/Pictures/$b/$c/)
			for f in $files
			do 
				current_loc=/home/pi/Documents/MaterialDecay/Pictures/$b/$c/$f
				/home/pi/.local/bin/aws s3 mv $current_loc s3://ice911/Data/"Material Decay Experiment, 6-19-2017"/Pictures/$b/$c
			done
		done
	done

fi