Code to be submitted by 16:00 on Wednesday 28th October.

We have a study where 150 participants have worn a wrist-worn accelerometer and wearable camera simultaneously for one day. The accelerometer logs data at a rate of 100Hz and the wearable camera logs data approximately every 15 seconds in response to sensory changes. The information is currently stored in csv files, but will need transfer to a database to facilitate quick and flexible interrogation. The wearable camera data has been annotated by a researcher into behavioural annotations (see P325Camera.csv) and the accelerometer data has been automatically processed into five second ‘epochs’ (see P325Accelerometer.csv).

Your task is to write a Linux-friendly python script to take the camera and accelerometer csv files as input and merge them together, so that each behavioural episode will have associated average acceleration data. The merged information should then be stored in a database of your choosing (fine to use sqlite for demonstration purposes). The python script should support subsequent querying of the database to describe the average acceleration associated with each behaviour type. You should also create concise documentation on how to run the code, any assumptions made in your approach, and any data quality issues encountered.

Please return your response as a ZIP file containing all relevant files and folders. This should be sent as an email attachment.  We will review the code as well as the completeness of the solution. There will be follow-up questions during the interview on how this code could be extended to support future machine learning analysis.

accelerometer
timestamp,acceleration,xRange,yRange,zRange,xStd,yStd,zStd,temp,samples,dataErrors,clipsBeforeCalibr,clipsAfterCalibr

camera
participant,startTime,endTime,source,annotations(comma-separated)

Linux-friendly python script to take the camera and accelerometer csv files as input and merge them together

parse csv
merge?
sqlite
    sensible schema
    sudo apt-get install sqliteman
	average acceleration associated with each behaviour type

support subsequent querying of the database to describe the average acceleration associated with each behaviour type
documentation how to run
assumptions made
data quality issues encountered


zip -r cpnp.zip cpnp
sent at 15:59:47...
Wed Oct 28 16:19:47 2015

