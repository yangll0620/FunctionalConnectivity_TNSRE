# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-22 15:09:24
# @Last Modified by:   yll
# @Last Modified time: 2018-11-23 10:01:33

from scipy.signal import hilbert
import numpy as np


def PhaseLockingValue(signal1, signal2):
	"""
		Phase locking value of two signals 
		@ parameter 
			signal1, signal2: n_epochs * n_times
		@ return
			PLV: phase locking value for signal1 and signal 2 (1 * times)
	"""
	n_times = signal1.shape[1]
	analytic_s1 = hilbert(signal1, axis = 1) # analytic_s1: : n_epochs * n_times
	analytic_s2 = hilbert(signal2, axis = 1) # analytic_s2: : n_epochs * n_times

	phase1_instant = np.unwrap(np.angle(analytic_s1)) # phase1_instant: : n_epochs * n_times
	phase2_instant = np.unwrap(np.angle(analytic_s2)) # phase2_instant: : n_epochs * n_times
	delta_phase = phase1_instant - phase2_instant # delta_phase2: : n_epochs * n_times

	PLV = np.absolute(np.sum(np.exp(1j * delta_phase), axis = 0))/n_times #  PLV: 1* n_times

	return PLV

def ciPLV(signal1, signal2):
	"""
		corrected imaginary Phase locking value
		ref:
			R. Bruña, F. Maestú, and E. Pereda, “Phase Locking Value revisited: teaching new tricks to an old dog,” 
			Journal of neural engineering, vol. 15, no. 5, p. 056011, 2018.
		@ parameter 
			signal1, signal2: n_epochs * n_times
		@ return
			ciPLV: corrected imaginary phase locking value for signal1 and signal 2 (1 * times) 
	"""
	n_times = signal1.shape[1]
	analytic_s1 = hilbert(signal1, axis = 1) # analytic_s1: : n_epochs * n_times
	analytic_s2 = hilbert(signal2, axis = 1) # analytic_s2: : n_epochs * n_times

	phase1_instant = np.unwrap(np.angle(analytic_s1)) # phase1_instant: : n_epochs * n_times
	phase2_instant = np.unwrap(np.angle(analytic_s2)) # phase2_instant: : n_epochs * n_times
	delta_phase = phase1_instant - phase2_instant # delta_phase2: : n_epochs * n_times

	ciPLV = np.imag(np.sum(np.exp(1j * delta_phase), axis = 0))/n_times #  PLV: 1* n_times

	return ciPLV