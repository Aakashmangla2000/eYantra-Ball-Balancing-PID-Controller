'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 4A of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Filename:			task_4a.py
# Functions:		find_path, read_start_end_coordinates
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the six available   ##
## modules for this task (numpy, opencv, os, traceback,     ##
## sys, json)												##
##############################################################
import numpy as np
import cv2
import os
import traceback
import sys
import json


# Import 'task_1b.py' file as module
try:
	import task_1b

except ImportError:
	print('\n[ERROR] task_1b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1b.py is present in this current directory.\n')
	sys.exit()
		
except Exception as e:
	print('Your task_1b.py throwed an Exception, kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	sys.exit()

##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################





##############################################################


def find_path(maze_array, start_coord, end_coord):
	"""
	Purpose:
	---
	Takes a maze array as input and calculates the path between the
	start coordinates and end coordinates.

	Input Arguments:
	---
	`maze_array` :   [ nested list of lists ]
		encoded maze in the form of a 2D array

	`start_coord` : [ tuple ]
		start coordinates of the path

	`end_coord` : [ tuple ]
		end coordinates of the path
	
	Returns:
	---
	`path` :  [ list of tuples ]
		path between start and end coordinates
	
	Example call:
	---
	path = find_path(maze_array, start_coord, end_coord)
	"""

	path = None

	################# ADD YOUR CODE HERE #################
	# print(maze_array)
	visited = []	#List to keep track of visited cells.
	queue = []      #Initialize a queue
	path = []
	solution = {}
	visited.append(start_coord)
	queue.append(start_coord)

	completed = False

	solution[start_coord] = start_coord[0],start_coord[1]

	while queue: 
		# print(queue)
		s = queue.pop(0)
		# s = queue[0] 
		# print(len(queue))
		if s == end_coord: 
			completed = True
			break

		x = maze_array[s[0]][s[1]]
		# print (s, end = " ") 
		if (s[0],s[1]-1) not in visited and s[1]-1 >= 0: 
			if (x == 0 or x == 4 or x == 2 or x == 6 or x == 8 or x == 10 or x == 14 or x == 12): 
				visited.append((s[0],s[1]-1))
				queue.append((s[0],s[1]-1))
				# print('left')
				cell = (s[0],s[1]-1)
				solution[cell] = s
		
		if (s[0]+1,s[1]) not in visited and s[0]+1 < 10: 
			if (x == 0 or x == 1 or x == 2 or x == 4 or x == 5 or x == 6 or x == 7 or x == 3): 
				visited.append((s[0]+1,s[1])) 
				queue.append((s[0]+1,s[1]))
				# print('down')
				cell = (s[0]+1,s[1])
				solution[cell] = s

		if (s[0],s[1]+1) not in visited and s[1]+1 < 10: 
			if (x == 0 or x == 1 or x == 2 or x == 8 or x == 9 or x == 10 or x == 11 or x == 3): 
				visited.append((s[0],s[1]+1))
				queue.append((s[0],s[1]+1))
				# print('right')
				cell = (s[0],s[1]+1)
				solution[cell] = s

		if (s[0]-1,s[1]) not in visited and s[0]-1 >= 0: 
			if (x == 0 or x == 1 or x == 4 or x == 5 or x == 8 or x == 9 or x == 12 or x == 13): 
				visited.append((s[0]-1,s[1]))
				queue.append((s[0]-1,s[1]))
				# print('up')
				cell = (s[0]-1,s[1])
				solution[cell] = s

	x,y = end_coord[0], end_coord[1]
	path.append(end_coord)
	while (x,y) != (start_coord[0], start_coord[1]): 
		try:
			path.append(solution[x,y])   
			x,y = solution[x, y]
		except:
			path.pop(0)
			path = None
			break
	
	######################################################
	# path = queue
	try:
		path.reverse()
	except:
		pass
	return path


def read_start_end_coordinates(file_name, maze_name):
	"""
	Purpose:
	---
	Reads the corresponding start and end coordinates for each maze image
	from the specified JSON file
	
	Input Arguments:
	---
	`file_name` :   [ str ]
		name of JSON file

	`maze_name` : [ str ]
		specify the maze image for which the start and end coordinates are to be returned.

	Returns:
	---
	`start_coord` : [ tuple ]
		start coordinates for the maze image

	`end_coord` : [ tuple ]
		end coordinates for the maze image
	
	Example call:
	---
	start, end = read_start_end_coordinates("start_end_coordinates.json", "maze00")
	"""

	start_coord = None
	end_coord = None

	################# ADD YOUR CODE HERE #################
	f = open(file_name,) 
	data = json.load(f) 

	start_coord = tuple(data[maze_name]['start_coord'])
	end_coord = tuple(data[maze_name]['end_coord'])

	# print(start_coord,end_coord)
	# print(data[maze_name])

	f.close() 

		
	######################################################

	return start_coord, end_coord


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

	file_num = 0

	maze_name = 'maze0' + str(file_num)

	# path to 'maze00.jpg' image file
	img_file_path = img_dir_path + maze_name + '.jpg'

	# read start and end coordinates from json file
	start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = task_1b.applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = task_1b.detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')

			path = find_path(maze_array, start_coord, end_coord)

			if (type(path) is list):

				print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
				print('\n============================================')

			else:
				print('\n Path does not exist between %s and %s' %(start_coord, end_coord))
		
		else:
			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:
		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1,10):

			maze_name = 'maze0' + str(file_num)

			img_file_path = img_dir_path + maze_name + '.jpg'

			# read start and end coordinates from json file
			start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')
	
			# read the 'maze00.jpg' image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = task_1b.applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = task_1b.detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')

					path = find_path(maze_array, start_coord, end_coord)

					if (type(path) is list):

						print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
						print('\n============================================')

					else:
						print('\n Path does not exist between %s and %s' %(start_coord, end_coord))

				else:
					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()

			else:				
				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()
	
	else:
		print()

