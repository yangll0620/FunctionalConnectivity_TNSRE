# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-22 10:57:38
# @Last Modified by:   yll
# @Last Modified time: 2018-11-26 11:47:19

import numpy as np 

def Rossler(x, a=10):
	x1, x2, x3 = x[0], x[1], x[2]
	x1_dot = -a*(x2 + x3)
	x2_dot = a * (x1 + 0.2 * x2)
	x3_dot = a * (0.2 + x1 * x3 - 5.7 * x3)
	
	x_dot = np.asarray([x1_dot, x2_dot, x3_dot])
	return x_dot

def Lorenz_byRossler1(y, C, x2_Rossler):
	''' @ parameter y: a vector 
	'''
	y1, y2, y3 = y[0], y[1], y[2]
	y1_dot = 10 * (y2 - y1)
	y2_dot = 28 * y1 -  y2 - y1 * y3 + C * np.square(x2_Rossler)
	y3_dot = y1 * y2 - (8/3) * y3
	
	y_dot = np.asarray([y1_dot, y2_dot, y3_dot])
	return y_dot

def Lorenz_byRossler2(xy, t, C=0.1):
	a = 10
	x1, x2, x3 = xy[0], xy[1], xy[2]
	y1, y2, y3 = xy[3], xy[4], xy[5]

	x1_dot = -a*(x2 + x3)
	x2_dot = a * (x1 + 0.2 * x2)
	x3_dot = a * (0.2 + x1 * x3 - 5.7 * x3)

	y1_dot = 10 * (y2 - y1)
	y2_dot = 28 * y1 -  y2 - y1 * y3 + C * np.square(x2)
	y3_dot = y1 * y2 - (8/3) * y3

	xy_dot = np.asarray([x1_dot, x2_dot, x3_dot, y1_dot,y2_dot,y3_dot])

	return xy_dot

def Colpitts(x, t, coupl_matrix,):
	""" the Colpitts Attractor 
		use x2

		ref: C. Carmeli, M. G. Knyazeva, G. M. Innocenti, and O. De Feo, “Assessment of EEG synchronization based on state-space analysis,” Neuroimage, vol. 25, no. 2, pp. 339–354, 2005.

		@ parameter 
			C_vector: a vector representing the coupling weight between this oscillator and all the others
			X2: a vector representing the x2 values of all the oscillators

		return x_dot: vecort [x1_dot, x2_dot, x3_dot]
	"""
	n_chns = int((len(x) + 1)/3)

	gs = np.random.uniform(4.006,4.428,(n_chns,))
	Qs = np.random.uniform(1.342,1.483,(n_chns,)) 
	alphas = np.random.uniform(0.949,0.999,(n_chns,)) 
	k = 0.5
	X2 = x[1:1 + n_chns * 3:3]
	for i_chn in range(n_chns):
		g, Q, alpha = gs[i_chn], Qs[i_chn], alphas[i_chn]
		C_vector = coupl_matrix[i_chn]
		 
		x1, x2, x3 = x[0 + i_chn * 3], x[1 + i_chn * 3], x[2 + i_chn * 3]
		x1_dot = g/(Q*(1-k)) * (alpha*(np.exp(-x2) -1) + x3)
		x2_dot = g/(Q*k)*((1 - alpha) *(np.exp(-x2) - 1) + x3) + np.dot(C_vector, (X2 - x2))
		x3_dot = -Q*k*(1-k)/g * (x1 + x2) - 1/Q * x3

		if i_chn == 0:
			x_dot = np.asarray([x1_dot, x2_dot, x3_dot])
		else:
			x_dot = np.append(x_dot,[x1_dot, x2_dot, x3_dot])

		del x1, x2, x3, x1_dot, x2_dot, x3_dot
		del g, Q, alpha, C_vector
	return x_dot