# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-22 10:57:38
# @Last Modified by:   yll
# @Last Modified time: 2018-11-22 16:25:56

import numpy as np 

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


def Colpitts(x1, x2, x3, X2, C, k = 0.5, g = 4.006, Q = 1.342, alpha = 0.949):
	""" the Colpitts Attractor 

		ref: C. Carmeli, M. G. Knyazeva, G. M. Innocenti, and O. De Feo, “Assessment of EEG synchronization based on state-space analysis,” Neuroimage, vol. 25, no. 2, pp. 339–354, 2005.

		@ parameter C: a vector representing the coupling weight between this oscillator and all the others
				X2: a vector representing the x2 values of all the oscillators

		return x1_dot, x2_dot, x3_dot
	"""
	x1_dot = g/(Q*(1-k)) * (alpha*(np.exp(-x2) -1) + x3)
	x2_dot = g/(Q*k)*((1 - alpha) *(np.exp(-x2) - 1) + x3) + np.dot(C, (X2 - x2))
	x3_dot = -Q*k*(1-k)/g * (x1 + x2) - 1/Q * x3

	return x1_dot, x2_dot, x3_dot