# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-22 14:54:25
# @Last Modified by:   yll
# @Last Modified time: 2018-11-23 10:40:43

from scipy.io import savemat
import numpy as np

import sys
sys.path.append("../")
from chaos_attractor import Colpitts
from GaussianNoise_SNR import GaussianNoise_SNR


def EEG_surr(cluster1, cluster2, Desired_SNR_dB = 20):
	""" generate the surrogated EEG data with coupling in cluster1 and cluster2

		@ parameter: 
			cluster1, cluster2: two 
		@ return eeg_noisy: the surrogated EEG data with desired_SNR_dB gaussian noise 

	"""
	dt = 0.01
	n_time = 10000

	n_chns = 64
	""" C: matrix (n_chns, n_chns) the weight matrix for each pair of channel i and j"""
	C = np.zeros((64,64))
	# intra-connection in cluster 1
	for i in range(len(cluster1)):
		i_chn = cluster1[i]
		for j in range(i+1, len(cluster1)):
			j_chn = cluster1[j]
			weight = np.random.uniform(3,5) # weight in range [3 5]
			C[i_chn][j_chn], C[i_chn][j_chn] = weight, weight
			del weight
	# intra-connection in cluster 2
	for i in range(len(cluster2)):
		i_chn = cluster2[i]
		for j in range(i+1, len(cluster2)):
			j_chn = cluster2[j]
			weight = np.random.uniform(3,5) # weight in range [3 5]
			C[i_chn][j_chn], C[i_chn][j_chn] = weight, weight
			del weight
	# interconnection
	weight = np.random.uniform(1,3) # weight in range [1 3]
	i_chn, j_chn = cluster1[-1], cluster2[0]
	C[i_chn][j_chn], C[j_chn][i_chn] = weight, weight

	# Need one more for the initial values
	X1 = np.empty((n_chns, n_time + 1))
	X2 = np.empty((n_chns, n_time + 1))
	X3 = np.empty((n_chns, n_time + 1))

	# Setting initial values
	X1[:,0] = np.random.random((n_chns,))
	X2[:,0] = np.random.random((n_chns,))
	X3[:,0] = np.random.random((n_chns,))

	# g, Q, alpha values for each channel
	g = np.random.uniform(4.006,4.428,(n_chns,))
	Q = np.random.uniform(1.342,1.483,(n_chns,)) 
	alpha = np.random.uniform(0.949,0.999,(n_chns,)) 
	k = 0.5

	# Stepping through "time".
	for i in range(n_time):
	    # Derivatives of the X, Y, Z state
	    for i_chn in range(n_chns):
	    	x1, x2, x3 = X1[i_chn, i], X2[i_chn, i], X3[i_chn,i]
	    	X2_i = X2[:, i] # samples of all the channels in time i
	    	x1_dot, x2_dot, x3_dot = Colpitts(x1, x2, x3, C[i_chn], X2_i, g = g[i_chn], Q = Q[i_chn], alpha = alpha[i_chn], k = k)

	    	X1[i_chn, i+1] = x1 + (x1_dot * dt)
	    	X2[i_chn, i+1] = x2 + (x2_dot * dt)
	    	X3[i_chn, i+1] = x3 + (x3_dot * dt)
	    	del x1, x2, x3, X2_i

	eeg = X2[:,-501:-1:5] # the transients were dropped out and down-sampled, eeg: n_chns * 100
	# add gaussian noise
	eeg_noisy = np.zeros(eeg.shape)
	for i_chn in range(n_chns):
		eeg_noisy[i_chn,:] = GaussianNoise_SNR(eeg[i_chn,:], Desired_SNR_dB)

	return eeg_noisy # eeg_noisy: n_chns * n_times


n_chns, n_times, n_iterate = 64,100,80
EEG_surrogate = np.zeros((n_chns, n_times, n_iterate))
cluster1 = np.asarray([8, 18, 19])
cluster2 = np.asarray([51, 52, 58])
for i_iterate in range(n_iterate):
	EEG_surrogate[:,:, i_iterate] = EEG_surr(cluster1, cluster2) # EEG_surrogate: n_chns * n_times * n_epochs 

savemat('EEG_surrogate.mat',{'EEG_surrogate':EEG_surrogate})
