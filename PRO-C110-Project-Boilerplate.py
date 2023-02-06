# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
#C:\Users\livcr\OneDrive\Pictures\projects\PRO-C110-Project-Boilerplate-main\110
import tensorflow as tf


# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		img = cv2.flip(frame , 1)
		
		
		
		#resize the frame
		img = cv2.resize(img,(255,255))
		# expand the dimensions
		ti = np.array(img,dtype = np.float32)

		ti = np.expand_dims(ti, axis= 0)
		# normalize it before feeding to the model
		ni = ti/255.0

		prediction = model.predict(ni)
		print(prediction)
		# get predictions from the model
		
		
		
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
