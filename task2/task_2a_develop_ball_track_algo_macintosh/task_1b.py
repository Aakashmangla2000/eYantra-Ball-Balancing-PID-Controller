'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[ NB_534 ]
# Author List:		[ Aakash Mangla ]
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def applyPerspectiveTransform(input_img):

	"""
	Purpose:
	---
	takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

	Input Arguments:
	---
	`input_img` :   [ numpy array ]
		maze image in the form of a numpy array
	
	Returns:
	---
	`warped_img` :  [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Example call:
	---
	warped_img = applyPerspectiveTransform(input_img)
	"""

	warped_img = None

	##############	ADD YOUR CODE HERE	##############

	cn = []
	areas = []

	# Reading same image in another 
	# variable and converting to gray scale. 
	# img = cv2.imread('maze06.jpg', cv2.IMREAD_GRAYSCALE) 
	img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	# Converting image to a binary image 
	# ( black and white only image). 
	_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) 
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(threshold,kernel,iterations = 2)
	dilation = cv2.dilate(erosion,kernel,iterations = 1)
	opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

	# Detecting contours in image. 
	contours, _= cv2.findContours(opening, cv2.RETR_TREE, 
								cv2.CHAIN_APPROX_SIMPLE) 

	area2 = 0
	area3 = 0
	t = 0

	# Going through every contours found in the image. 
	for cnt in contours[1::]: 
		area = cv2.contourArea(cnt)
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		# print(len(approx))
		if area > area2:
			if area > area2 and area < area3:
				area2 = area
				cn = []
				t = 1
			elif area < area2 and area < area3:
				pass
			else:
				area3 = area
	# 		area2 = area
	# 		area3 = area
			cn = []
			t = 1
		areas.append(area)
		approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 

		# draws boundary of contours. 
		cv2.drawContours(input_img, [approx], 0, (0, 0, 255), 5) 

		# Used to flatted the array containing 
		# the co-ordinates of the vertices. 
		n = approx.ravel() 
		i = 0
		
		if len(approx) == 4 and t == 1:
			for j in n : 
				if(i % 2 == 0): 
					x = n[i] 
					y = n[i + 1] 
	# 				if t == 1:
	# 					cn.append([x,y])

					cn.append([x,y])            
					string = str(x) + " " + str(y) 
				i = i + 1; t = 0
		t = 0    

	cv2.imshow('image',input_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	for i in range(len(cn)): 
		if cn[i][0] > 100 and cn[i][1] < 100:
			x2 = cn[i][0]
			y2 = cn[i][1]
		if cn[i][0] > 100 and cn[i][1] > 100:
			x4 = cn[i][0]
			y4 = cn[i][1]
		if cn[i][0] < 100 and cn[i][1] > 100:
			x3 = cn[i][0]
			y3 = cn[i][1]
		if cn[i][0] < 100 and cn[i][1] < 100:
			x1 = cn[i][0]
			y1 = cn[i][1]

	# img = cv2.imread("maze06.jpg")
	# pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
	
	pts1 = np.float32([[55, 55], [970, 55], [55, 970], [970, 970]])
	pts2 = np.float32([[0, 0], [1280, 0], [0, 1280], [1280, 1280]])

	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	result = cv2.warpPerspective(input_img, matrix, (1280, 1280))
	warped_img = result

	return warped_img


def detectMaze(warped_img):

	"""
	Purpose:
	---
	takes the warped maze image as input and returns the maze encoded in form of a 2D array

	Input Arguments:
	---
	`warped_img` :    [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Returns:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array

	Example call:
	---
	maze_array = detectMaze(warped_img)
	"""

	maze_array = []

	##############	ADD YOUR CODE HERE	##############
	
	ret,im = cv2.threshold(warped_img,127,255,cv2.THRESH_BINARY)
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(im,kernel,iterations = 2)
	dilation = cv2.dilate(erosion,kernel,iterations = 1)
	opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

	r = opening
	size = 51.2

	mat = []

	for i in range(10):
		mat.append([])
		for j in range(10):
			block = r[int(i*size):int((i+1)*size),int(j*size):int((j+1)*size)]
			up    = (not bool(np.all(block[0,int(size/2)]))) *2
			down  = (not bool(np.all(block[int(size-1),int(size/2)])))*8
			left  = (not bool(np.all(block[int(size/2),0]))) *1
			right = (not bool(np.all(block[int(size/2),int(size-1)])))*4
			total = up + down + left + right
			
			mat[i].append(total)
	
	maze_array = mat
	return maze_array
	##################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

