'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 5 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD (now MOE) project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          [ Team-ID ]
# Author List:      [ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         task_5.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

# NOTE: Make sure you do NOT call sys.exit() in this code.

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
import math
import json
##############################################################

# Importing the sim module for Remote API connection with CoppeliaSim
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	

#Import 'task_1b.py' file as module
try:
	import task_1b

except ImportError:
	print('\n[ERROR] task_1b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1b.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_1b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_1a_part1.py' file as module
try:
	import task_1a_part1

except ImportError:
	print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1a_part1.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_1a_part1.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_2a.py' file as module
try:
	import task_2a

except ImportError:
	print('\n[ERROR] task_2a.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_2a.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_2a.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	

# Import 'task_2b.py' file as module
try:
	import task_2b

except ImportError:
	print('\n[ERROR] task_2b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_2b.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_2b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	

# Import 'task_3.py' file as module
try:
	import task_3

except ImportError:
	print('\n[ERROR] task_3.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_3.py is present in this current directory.\n')
	

except Exception as e:
	print('Your task_3.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_4a.py' file as module
try:
	import task_4a

except ImportError:
	print('\n[ERROR] task_4a.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_4a.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_4a.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)


try:
	import task_4b

except ImportError:
	print('\n[ERROR] task_4b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_4b.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_4b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)

##############################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    send_color_and_collection_box_identified
#        Inputs:    ball_color and collection_box_name
#       Outputs:    None
#       Purpose:    1. This function should only be called when the task is being evaluated using
# 					   test executable.
#					2. The format to send the data is as follows:
#					   'color::collection_box_name'				   
def send_color_and_collection_box_identified(ball_color, collection_box_name):

	global client_id

	color_and_cb = ball_color + '::' + collection_box_name
	inputBuffer = bytearray()
	return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id,'evaluation_screen_respondable_1',
							sim.sim_scripttype_childscript,'color_and_cb_identification',[],[],color_and_cb,inputBuffer,sim.simx_opmode_blocking)

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################

maze_array_1,maze_array_2,maze_array_3,maze_array_4 = [],[],[],[]
path_1,path_2,path_3,path_4 = [],[],[],[]

ball_col = None
ball_count = 0

def maze_array_and_path(num,start,end): 
	img_file_path = 'maze_t' + str(num) + '.jpg'
	if os.path.exists(img_file_path): 

		task_4b.start_coord = start
		task_4b.end_coord = end
		    		
		try:
			maze_array,path = task_4b.calculate_path_from_maze_image(img_file_path)
		
		except Exception:
			print('\n[ERROR] Your calculate_path_from_maze_image() function throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
	else:
		print('\n[ERROR] maze_t1.jpg not found.')
		print('Your current directory is: ', os.getcwd())
		sys.exit()

	return maze_array,path

def start_vision_sensors2(table_num): 
	try:
			vision_sensor_image_5, image_resolution_5, return_code = task_2a.get_vision_sensor_image2(task_3.vision_sensor_handle_5)
			vision_sensor_image_4, image_resolution_4, return_code = task_2a.get_vision_sensor_image(task_3.vision_sensor_handle_4)
			vision_sensor_image_1, image_resolution_1, return_code = task_2a.get_vision_sensor_image(task_3.vision_sensor_handle_1)


			if ((return_code == sim.simx_return_ok) and (len(image_resolution_4) == 2) and (len(vision_sensor_image_4) > 0)):
				# print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')
				# Get the transformed vision sensor image captured in correct format
				try:
					transformed_image_1 = task_2a.transform_vision_sensor_image(vision_sensor_image_1, image_resolution_1)
					transformed_image_4 = task_2a.transform_vision_sensor_image(vision_sensor_image_4, image_resolution_4)
					transformed_image_5 = task_2a.transform_vision_sensor_image(vision_sensor_image_5, image_resolution_5)

					if (type(transformed_image_4) is np.ndarray): 
						# cv2.imshow('transformed image', transformed_image_5)
						# cv2.waitKey(0)
						# cv2.destroyAllWindows()

						# Get the resultant warped transformed vision sensor image after applying Perspective Transform
						try:
							warped_img_1 = task_1b.applyPerspectiveTransform(transformed_image_1)
							warped_img_4 = task_1b.applyPerspectiveTransform(transformed_image_4)
							warped_img_5 = task_1b.applyPerspectiveTransform(transformed_image_5)

							# cv2.imshow('transformed image', warped_img_5)
							# cv2.waitKey(0)
							# cv2.destroyAllWindows()
							
							if (type(warped_img_4) is np.ndarray):
								
								# Get the 'shapes' dictionary by passing the 'warped_img' to scan_image function
								try:
									shapes_1 = task_1a_part1.scan_image(warped_img_1)
									shapes_4 = task_1a_part1.scan_image(warped_img_4)
									ball_color = task_1a_part1.scan_image2(warped_img_5)

									if (type(shapes_4) is dict and shapes_4!={}):
										
										global ball_col, ball_count
										# Storing the detected x and y centroid in center_x and center_y variable repectively
										center_x_4 = shapes_4['Circle'][1]
										center_y_4 = shapes_4['Circle'][2]

										center_x_1 = shapes_1['Circle'][1]
										center_y_1 = shapes_1['Circle'][2]

										if(ball_color != None): 
											ball_col = ball_color
											return ball_color
											# ball_count += 1
										# if(entered == 0): 
										# 	if(center_x == 0): 
										# 		print('no')
										# 		return 0
										# print('yes')
										# print('\nShapes detected by Vision Sensor are: ')
										print(ball_col,ball_count)

									elif(type(shapes_4) is not dict):
										print('\n[ERROR] scan_image function returned a ' + str(type(shapes_4)) + ' instead of a dictionary.')
										print('Stop the CoppeliaSim simulation manually.')
										print()
										sys.exit()
								
								except Exception:
									print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
							
							else:
								print('\n[ERROR] applyPerspectiveTransform function is not configured correctly, check the code.')
								print('Stop the CoppeliaSim simulation manually.')
								print()
								sys.exit()
						
						except Exception:
							print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception. Kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()

					else:
						print('\n[ERROR] transform_vision_sensor_image function in task_2a.py is not configured correctly, check the code.')
						print('Stop the CoppeliaSim simulation manually.')
						print()
						sys.exit()

				except Exception:
					print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
					print('Stop the CoppeliaSim simulation manually.\n')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
			try: 
				# maze_array_1,path_1 = maze_array_and_path(1,(0,4),(4,9))
				# maze_array_4,path_4 = maze_array_and_path(4,(0,5),(5,9))

				# return_code = task_2b.send_data(client_id,maze_array_4,4)
				# return_code = task_2b.send_data(client_id,maze_array_1,1)

				# task_3.control_logic(center_x_1,center_y_1,center_x_4,center_y_4,table_num)
				# cnt += 1
				# print(cnt)
				# print('control')
				pass
			
			except:
				print('\n[ERROR] Your control_logic function throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()

	except Exception:
			print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()


def start_vision_sensors(table_num): 
	try:
			vision_sensor_image_5, image_resolution_5, return_code = task_2a.get_vision_sensor_image2(task_3.vision_sensor_handle_5)

			if ((return_code == sim.simx_return_ok) and (len(image_resolution_5) == 2) and (len(vision_sensor_image_5) > 0)):
				# print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')
				# Get the transformed vision sensor image captured in correct format
				try:
					transformed_image_5 = task_2a.transform_vision_sensor_image(vision_sensor_image_5, image_resolution_5)

					if (type(transformed_image_5) is np.ndarray): 
						# Get the resultant warped transformed vision sensor image after applying Perspective Transform
						try:
							warped_img_5 = task_1b.applyPerspectiveTransform(transformed_image_5)
							
							if (type(warped_img_5) is np.ndarray):
								
								# Get the 'colour' by passing the 'warped_img' to scan_image function
								try:
																			
									global ball_col, ball_count
									ball_color = task_1a_part1.scan_image2(warped_img_5)

									if(ball_color != None): 
										ball_col = ball_color
										return ball_color

									# print(ball_col,ball_count)

								
								except Exception:
									print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
							
							else:
								print('\n[ERROR] applyPerspectiveTransform function is not configured correctly, check the code.')
								print('Stop the CoppeliaSim simulation manually.')
								print()
								sys.exit()
						
						except Exception:
							print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception. Kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()

					else:
						print('\n[ERROR] transform_vision_sensor_image function in task_2a.py is not configured correctly, check the code.')
						print('Stop the CoppeliaSim simulation manually.')
						print()
						sys.exit()

				except Exception:
					print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
					print('Stop the CoppeliaSim simulation manually.\n')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()

	except Exception:
			print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

def get_maze_array(maze_num):

	# read the 'maze00.jpg' image file
	input_img = cv2.imread('maze_t' + str(maze_num) + '.jpg')

	if type(input_img) is np.ndarray:

		try:
			# get the resultant warped maze image after applying Perspective Transform
			warped_img = task_1b.applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				try:
					# get the encoded maze in the form of a 2D array
					maze_array = task_1b.detectMaze(warped_img)

					if (type(maze_array) is list) and (len(maze_array) == 10):
						print('\nEncoded Maze Array = %s' % (maze_array))
						print('\n============================================')

					else:
						print('\n[ERROR] maze_array returned by detectMaze function in \'task_1b.py\' is not returning maze array in expected format!, check the code.')
						print()
						sys.exit()
				
				except Exception:
					print('\n[ERROR] Your detectMaze function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
			else:
				print('\n[ERROR] applyPerspectiveTransform function in \'task_1b.py\' is not returning the warped maze image in expected format!, check the code.')
				print()
				sys.exit()

		except Exception:
			print('\n[ERROR] Your applyPerspectiveTransform function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
	
	else:
		print('\n[ERROR] maze_t' + str(maze_num) + '.jpg was not read correctly, something went wrong!')
		print()
		sys.exit()

	return maze_array

##############################################################


def main(rec_client_id):
	"""
	Purpose:
	---

	Teams are free to design their code in this task.
	The test executable will only call this function of task_5.py.
	init_remote_api_server() and exit_remote_api_server() functions are already defined
	in the executable and hence should not be called by the teams.
	The obtained client_id is passed to this function so that teams can use it in their code.

	However NOTE:
	Teams will have to call start_simulation() and stop_simulation() function on their own. 

	Input Arguments:
	---
	`rec_client_id` 	:  integer
		client_id returned after calling init_remote_api_server() function from the executable.
	
	Returns:
	---
	None

	Example call:
	---
	main(rec_client_id)
	
	"""
	##############	ADD YOUR CODE HERE	##############
	global maze_array_1,maze_array_4,path_1,path_4


	maze_array_1 = get_maze_array(1)
	maze_array_4 = get_maze_array(4)

	try:
		# Send maze array data to CoppeliaSim via Remote API
		return_code = task_2b.send_data(client_id,maze_array_4,4)
		return_code = task_2b.send_data(client_id,maze_array_1,1)

	except Exception: 
		print(Exception)


	# Starting the Simulation
	try:
		return_code = task_2a.start_simulation()

		if (return_code == sim.simx_return_novalue_flag):
			print('\nSimulation started correctly in CoppeliaSim.')
			
			# Storing the required handles in respective global variables.
			try:
				task_3.init_setup(client_id)
			
			except Exception:
				print('\n[ERROR] Your init_setup() function throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually if started.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
			print('start_simulation function in task_2a.py is not configured correctly, check the code!')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your start_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()

	#Main Logic
	try:
		global ball_count
		
		color = None

		#For X number of balls
		while(ball_count < 1): 

			#Detecting the ball and its color
			while(color == None):
				color = start_vision_sensors(1)

			f = open('ball_details.json',) 
			data = json.load(f) 
			
			print(data[color])

			f.close() 
			

			time_prev = 0
			total_time = 0
			test = 0

			maze_array_4, path_4 = maze_array_and_path(4,(0,5),(5,9))
			pixel_path_4 = task_4b.convert_path_to_pixels(path_4)

			maze_array_1, path_1 = maze_array_and_path(1,(5,0),(0,4))
			pixel_path_1 = task_4b.convert_path_to_pixels(path_1)

			# Running for 80 seconds
			while(test <= 0): 
				time_new=time.time()
				total_time = (time_new - time_prev)
				time_prev=time_new
				if(total_time < 1): 
					test += total_time

			task_4b.traverse_path(pixel_path_4,4)
			task_4b.traverse_path(pixel_path_1,1)
			# print(color)
			ball_count += 1
			color = None
	
	except Exception:
		print('\n[ERROR] Your traverse_path() function throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()


	#Stopping the simulation
	try:
		return_code = task_2a.stop_simulation()
		
		if (return_code == sim.simx_return_novalue_flag):
			print('\nSimulation stopped correctly.')

			# Stop the Remote API connection with CoppeliaSim server
			try:
				task_2a.exit_remote_api_server()

				if (task_2a.start_simulation() == sim.simx_return_initialize_error_flag):
					print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

				else:
					print('\n[ERROR] Failed disconnecting from Remote API server!')
					print('[ERROR] exit_remote_api_server function in task_2a.py is not configured correctly, check the code!')

			except Exception:
				print('\n[ERROR] Your exit_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
			print('[ERROR] stop_simulation function in task_2a.py is not configured correctly, check the code!')
			print('Stop the CoppeliaSim simulation manually.')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your stop_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()

	##################################################


# Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the main(rec_client_id) function written by teams when they
#					run task_5.py only.

# NOTE: Write your solution ONLY in the space provided in the above functions. This function should not be edited.
if __name__ == "__main__":

	client_id = task_2a.init_remote_api_server()
	main(client_id)
