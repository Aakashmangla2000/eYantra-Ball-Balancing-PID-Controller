# # # # # # print(lx-nx)
# # # # # 	# # print(a1,'a1',a2,'a2')

# # # # # 	# angle1 = 0.174533
# # # # # 	# angle2 = 0.174533

# # # # # 	# a = 0.174533


# # # # # 	# if(abs(lx-nx) > 50): 
# # # # # 	# 	angle1 = angle1 + a
	
# # # # # 	# elif(abs(lx-nx) < 50): 
# # # # # 	# 	angle1 = angle1 - a

# # # # # 	# if(abs(ly-ny) > 50): 
# # # # # 	# 	angle2 = angle2 + a
	
# # # # # 	# elif(abs(ly-ny) < 50): 
# # # # # 	# 	angle2 = angle2 - a
	
# # # # # 	# print(angle1,angle2)


# # # # # 	# if(nx > 0): 
# # # # # 	# 	a1 = a1+angle1
# # # # # 	# 	a3 = a3-angle1
# # # # # 	# 	return_code = sim.simxSetJointTargetPosition(client_id, rj3,a3,sim.simx_opmode_oneshot)
# # # # # 	# 	# return_code = sim.simxSetJointTargetPosition(client_id, rj1,a1,sim.simx_opmode_oneshot)
		
# # # # # 	# elif(nx < 0): 
# # # # # 	# 	a1 = a1-angle1
# # # # # 	# 	a3 = a3+angle1
# # # # # 	# 	return_code = sim.simxSetJointTargetPosition(client_id, rj3,a3,sim.simx_opmode_oneshot)
# # # # # 	# 	# return_code = sim.simxSetJointTargetPosition(client_id, rj1,a1,sim.simx_opmode_oneshot)
		

# # # # # 	# if(ny < 0): 
# # # # # 	# 	a2 = a2-angle2
# # # # # 	# 	a4 = a4+angle2
# # # # # 	# 	return_code = sim.simxSetJointTargetPosition(client_id, rj2,a2,sim.simx_opmode_oneshot)
# # # # # 	# 	# return_code = sim.simxSetJointTargetPosition(client_id, rj4,a4,sim.simx_opmode_oneshot)
		
# # # # # 	# else: 
# # # # # 	# 	a2 = a2+angle2
# # # # # 	# 	a4 = a4-angle2
# # # # # 	# 	return_code = sim.simxSetJointTargetPosition(client_id, rj2,a2,sim.simx_opmode_oneshot)
# # # # # 	# 	# return_code = sim.simxSetJointTargetPosition(client_id, rj4,a4,sim.simx_opmode_oneshot)

# # # # # 	# lx = nx
# # # # # 	# ly = ny


# # # # #     # 1 with time tweek 

# # # # #     global set_point, client_id, lx,ly,	a1,a2,a3,a4
# # # # # 	global timenow,previous_error_x,previous_error_y,pid_i_x,pid_i_y,sum_err_x,sum_err_y,time_previous, lastInput

# # # # # 	# if(center_x != 0 and center_y != 0): 
# # # # # 	# 	nx,ny = center_x-1063,center_y-1063
# # # # # 	# else: 
# # # # # 	# 	nx,ny = 0,0
# # # # # 	# ##############	ADD YOUR CODE HERE	##############
	
	
# # # # # 	timenow=time.time()
# # # # # 	elapsedTime=timenow-time_previous
# # # # # 	time_previous=timenow

# # # # # 	#PID calcuation
# # # # # 	error_x=(set_point[0]-center_x)/1
# # # # # 	#Proportional
# # # # # 	pid_p_x=kp*error_x
	
# # # # # 	#Integral
# # # # # 	sum_err_x += error_x
# # # # # 	pid_i_x=(ki*error_x)

# # # # # 	#Derivative
# # # # # 	pid_d_x=kd*((error_x-previous_error_x))

# # # # # 	# print(pid_d,'pid')
# # # # # 	previous_error_x=error_x
# # # # # 	PID_x = pid_p_x + pid_i_x + pid_d_x
# # # # # 	servo_signal_x=90+PID_x

# # # # # 	#PID calcuation
# # # # # 	error_y=(set_point[1]-center_y)/1

# # # # # 	#Proportional
# # # # # 	pid_p_y=kp*error_y
# # # # # 	#Integral

# # # # # 	sum_err_y += error_y
# # # # # 	pid_i_y=(ki*sum_err_y*elapsedTime)
# # # # # 	#Derivative

# # # # # 	pid_d_y=kd*((error_y-previous_error_y)/elapsedTime)

# # # # # 	# print(pid_d,'pid')
# # # # # 	previous_error_y=error_y
# # # # # 	PID_y = pid_p_y + pid_i_y + pid_d_y
# # # # # 	servo_signal_y=90+PID_y

# # # # # 	pi=22/7
# # # # # 	radian_x = PID_x*(pi/180)
# # # # # 	radian_y = PID_y*(pi/180)

# # # # # 	# print(PID_x,PID_y)
# # # # # 	# print('time', elapsedTime)
# # # # # 	# print(center_x,center_y)
# # # # # 	print(set_point)
	
# # # # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj3,radian_x,sim.simx_opmode_oneshot)
# # # # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj4,radian_y,sim.simx_opmode_oneshot)

# # # # #     #2 with derivative kick

# # # # global set_point, client_id, lx,ly,	a1,a2,a3,a4
# # # # 	global timenow,previous_error_x,previous_error_y,pid_i_x,pid_i_y,sum_err_x,sum_err_y,time_previous, lastInput_x,lastInput_y

# # # # 	# if(center_x != 0 and center_y != 0): 
# # # # 	# 	nx,ny = center_x-1063,center_y-1063
# # # # 	# else: 
# # # # 	# 	nx,ny = 0,0
# # # # 	# ##############	ADD YOUR CODE HERE	##############
	
	
# # # # 	timenow=time.time()
# # # # 	elapsedTime=timenow-time_previous
# # # # 	time_previous=timenow

# # # # 	#PID calcuation
# # # # 	error_x=(set_point[0]-center_x)/1
# # # # 	#Proportional
# # # # 	pid_p_x=kp*error_x
	
# # # # 	#Integral
# # # # 	sum_err_x += error_x
# # # # 	pid_i_x=(ki*error_x)

# # # # 	#Derivative
# # # # 	pid_d_x=kd*((center_x-lastInput_x))

# # # # 	# print(pid_d,'pid')
# # # # 	previous_error_x=error_x
# # # # 	PID_x = pid_p_x + pid_i_x - pid_d_x
# # # # 	servo_signal_x=90+PID_x

# # # # 	#PID calcuation
# # # # 	error_y=(set_point[1]-center_y)/1

# # # # 	#Proportional
# # # # 	pid_p_y=kp*error_y
# # # # 	#Integral

# # # # 	sum_err_y += error_y
# # # # 	pid_i_y=(ki*sum_err_y)
# # # # 	#Derivative

# # # # 	pid_d_y=kd*((center_y-lastInput_y))

# # # # 	# print(pid_d,'pid')
# # # # 	previous_error_y=error_y
# # # # 	PID_y = pid_p_y + pid_i_y - pid_d_y
# # # # 	servo_signal_y=90+PID_y

# # # # 	pi=22/7
# # # # 	radian_x = PID_x*(pi/180)
# # # # 	radian_y = PID_y*(pi/180)

# # # # 	# print(PID_x,PID_y)
# # # # 	# print('time', elapsedTime)
# # # # 	# print(center_x,center_y)
# # # # 	print(set_point)
	
# # # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj3,radian_x,sim.simx_opmode_oneshot)
# # # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj4,radian_y,sim.simx_opmode_oneshot)

# # # # 3 On-The-Fly Tuning Changes 

# # # global set_point, client_id, lx,ly,	a1,a2,a3,a4
# # # 	global timenow,previous_error_x,previous_error_y,pid_i_x,pid_i_y,sum_err_x,sum_err_y,time_previous, lastInput_x,lastInput_y
# # # 	global ITerm_x,ITerm_y
# # # 	# if(center_x != 0 and center_y != 0): 
# # # 	# 	nx,ny = center_x-1063,center_y-1063
# # # 	# else: 
# # # 	# 	nx,ny = 0,0
# # # 	# ##############	ADD YOUR CODE HERE	##############
	
	
# # # 	timenow=time.time()
# # # 	elapsedTime=timenow-time_previous
# # # 	time_previous=timenow

# # # 	#PID calcuation
# # # 	error_x=(set_point[0]-center_x)/1
# # # 	#Proportional
# # # 	pid_p_x=kp*error_x
	
# # # 	#Integral
# # # 	sum_err_x += error_x
# # # 	pid_i_x += (ki*error_x)

# # # 	#Derivative
# # # 	pid_d_x=kd*((center_x-lastInput_x))

# # # 	# print(pid_d,'pid')
# # # 	previous_error_x=error_x
# # # 	PID_x = pid_p_x + pid_i_x - pid_d_x
# # # 	servo_signal_x=90+PID_x

# # # 	#PID calcuation
# # # 	error_y=(set_point[1]-center_y)/1

# # # 	#Proportional
# # # 	pid_p_y=kp*error_y

# # # 	#Integral
# # # 	sum_err_y += error_y
# # # 	pid_i_y += (ki*error_y)

# # # 	#Derivative
# # # 	pid_d_y=kd*((center_y-lastInput_y))

# # # 	# print(pid_d,'pid')
# # # 	previous_error_y=error_y
# # # 	PID_y = pid_p_y + pid_i_y - pid_d_y
# # # 	servo_signal_y=90+PID_y

# # # 	pi=22/7
# # # 	radian_x = PID_x*(pi/180)
# # # 	radian_y = PID_y*(pi/180)

# # # 	# print(PID_x,PID_y)
# # # 	# print('time', elapsedTime)
# # # 	# print(center_x,center_y)
# # # 	print(set_point)
	
# # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj1,radian_x,sim.simx_opmode_oneshot)
# # # 	return_code = sim.simxSetJointTargetPosition(client_id, rj2,radian_y,sim.simx_opmode_oneshot)

# # # 4 Reset Windup Mitigation 

# # global set_point, client_id, lx,ly,	a1,a2,a3,a4
# # 	global timenow,previous_error_x,previous_error_y,pid_i_x,pid_i_y,sum_err_x,sum_err_y,time_previous, lastInput_x,lastInput_y
# # 	global ITerm_x,ITerm_y

# # 	outMax = 90
# # 	outMin = -90
# # 	# if(center_x != 0 and center_y != 0): 
# # 	# 	nx,ny = center_x-1063,center_y-1063
# # 	# else: 
# # 	# 	nx,ny = 0,0
# # 	# ##############	ADD YOUR CODE HERE	##############
	
	
# # 	timenow=time.time()
# # 	elapsedTime=timenow-time_previous
# # 	time_previous=timenow

# # 	#PID calcuation
# # 	error_x=(set_point[0]-center_x)/1
# # 	#Proportional
# # 	pid_p_x=kp*error_x
	
# # 	#Integral
# # 	sum_err_x += error_x
# # 	pid_i_x += (ki*error_x)
# # 	if(pid_i_x > outMax): 
# # 		pid_i_x = outMax;
# # 	elif(pid_i_x < outMin): 
# # 		pid_i_x = outMin;

# # 	#Derivative
# # 	pid_d_x=kd*((center_x-lastInput_x))

# # 	# print(pid_d,'pid')
# # 	previous_error_x=error_x
# # 	PID_x = pid_p_x + pid_i_x - pid_d_x
# # 	if(PID_x > outMax): 
# # 		PID_x = outMax;
# # 	elif(PID_x < outMin): 
# # 		PID_x = outMin;
# # 	servo_signal_x=90+PID_x

# # 	#PID calcuation
# # 	error_y=(set_point[1]-center_y)/1

# # 	#Proportional
# # 	pid_p_y=kp*error_y

# # 	#Integral
# # 	sum_err_y += error_y
# # 	pid_i_y += (ki*error_y)
# # 	if(pid_i_y > outMax): 
# # 		pid_i_y = outMax;
# # 	elif(pid_i_y < outMin): 
# # 		pid_i_y = outMin;

# # 	#Derivative
# # 	pid_d_y=kd*((center_y-lastInput_y))

# # 	# print(pid_d,'pid')
# # 	previous_error_y=error_y
# # 	PID_y = pid_p_y + pid_i_y - pid_d_y
# # 	if(PID_y > outMax): 
# # 		PID_y = outMax;
# # 	elif(PID_y < outMin): 
# # 		PID_y = outMin;
# # 	servo_signal_y=90+PID_y

# # 	pi=22/7
# # 	radian_x = PID_x*(pi/180)
# # 	radian_y = PID_y*(pi/180)

# # 	print(PID_x,PID_y)
# # 	# print('time', elapsedTime)
# # 	# print(center_x,center_y)
# # 	print(set_point)
	
# # 	return_code = sim.simxSetJointTargetPosition(client_id, rj3,radian_x,sim.simx_opmode_oneshot)
# # 	return_code = sim.simxSetJointTargetPosition(client_id, rj4,radian_y,sim.simx_opmode_oneshot)

# # 5 On/Off (Auto/Manual) 

# # 6 Initialization 

# # 7 Controller Direction

# # 8 Controller Direction



# # LATEST CODE

# global set_point, client_id, lx,ly,	a1,a2,a3,a4
# 	global timenow,previous_error_x,previous_error_y,pid_i_x,pid_i_y,sum_err_x,sum_err_y,time_previous, lastInput_x,lastInput_y
# 	global ITerm_x,ITerm_y

# 	outMax = 360
# 	outMin = -360
# 	# if(center_x != 0 and center_y != 0): 
# 	# 	nx,ny = center_x-1063,center_y-1063
# 	# else: 
# 	# 	nx,ny = 0,0
# 	# ##############	ADD YOUR CODE HERE	##############

# 	# if angle > 0:
#     #     if angle > math.pi:
#     #         return angle - 2*math.pi
#     # else:
#     #     if angle < -math.pi:
#     #         return angle + 2*math.pi
#     # return angle
	
	
# 	timenow=time.time()
# 	elapsedTime=timenow-time_previous
# 	time_previous=timenow

# 	#PID calcuation
# 	error_x=(set_point[0]-center_x)/1
# 	#Proportional
# 	pid_p_x=kpx*error_x
	
# 	#Integral
# 	sum_err_x += error_x
# 	pid_i_x += (kix*error_x)
# 	# if(pid_i_x > outMax): 
# 	# 	pid_i_x = outMax;
# 	# elif(pid_i_x < outMin): 
# 	# 	pid_i_x = outMin;

# 	#Derivative
# 	pid_d_x=kdx*((center_x-lastInput_x))

# 	# print(pid_d,'pid')
# 	previous_error_x=error_x
# 	PID_x = pid_p_x + pid_i_x - pid_d_x
# 	# if(PID_x > outMax): 
# 	# 	PID_x = outMax;
# 	# elif(PID_x < outMin): 
# 	# 	PID_x = outMin;
# 	servo_signal_x=90+PID_x

# 	#PID calcuation
# 	error_y=(set_point[1]-center_y)/1

# 	#Proportional
# 	pid_p_y=kpy*error_y

# 	#Integral
# 	sum_err_y += error_y
# 	pid_i_y += (kiy*error_y)
# 	# if(pid_i_y > outMax): 
# 	# 	pid_i_y = outMax;
# 	# elif(pid_i_y < outMin): 
# 	# 	pid_i_y = outMin;

# 	#Derivative
# 	pid_d_y=kdy*((center_y-lastInput_y))

# 	# print(pid_d,'pid')
# 	previous_error_y=error_y
# 	PID_y = pid_p_y + pid_i_y - pid_d_y
# 	# if(PID_y > outMax): 
# 	# 	PID_y = outMax;
# 	# elif(PID_y < outMin): 
# 	# 	PID_y = outMin;
# 	servo_signal_y=90+PID_y

# 	pi=22/7

# 	PID_x = PID_x*(pi/180)
# 	PID_y = PID_y*(pi/180)
	
# 	if PID_x > 0: 
# 		if PID_x > pi: 
# 			PID_x = PID_x - 2*pi
# 	else: 
# 		if PID_x < -pi: 
# 			PID_x = PID_x + 2*pi

# 	if PID_y > 0: 
# 		if PID_y > pi: 
# 			PID_y = PID_y - 2*pi
# 	else: 
# 		if PID_y < -pi: 
# 			PID_y = PID_y + 2*pi

	

# 	print(PID_x,PID_y)
# 	# print('time', elapsedTime)
# 	# print(center_x,center_y)
# 	# print(set_point)
	
# 	return_code = sim.simxSetJointTargetPosition(client_id, rj1,PID_x,sim.simx_opmode_oneshot)
# 	return_code = sim.simxSetJointTargetPosition(client_id, rj4,PID_y,sim.simx_opmode_oneshot)


#0.05,0,0.1

# distance

# kpx = 0.045
# kix = 0.0
# kdx = 0.065

# float kp[] = {0.175,0.175,0.175};
# float kd[] = {0.10,0.10,0.10};

# 0.1,001,0.1

# P       :0.06
# I       :0.19
# D       :0.06
# out_min :-35
# out_max :25

# 1, 0.2, 0.4,

# kp=0.4
# ki=0
# kd=0.1

# const int32_t Px = 120;
# const int32_t Ix = 5;
# const int32_t Dx = 240;