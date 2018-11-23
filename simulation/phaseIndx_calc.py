# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-23 10:36:21
# @Last Modified by:   yll
# @Last Modified time: 2018-11-23 12:24:34


import numpy as np 
from scipy.io import loadmat, savemat
import pandas as pd

import sys
sys.path.append("../")
from synchronization_index import PhaseLockingValue, ciPhaseLockingValue

# load simulated EEG data
data = loadmat('./EEG_surrogate.mat')
eeg = data['EEG_surrogate'] # eeg : n_chns * n_times * n_epochs
n_chns, n_times, n_epochs = eeg.shape

# calculate phase synchronization index
# PLV value
PLV = np.zeros((n_chns,n_chns, n_times)) # PLV: n_chns * n_chns * n_times
for i_chn in range(n_chns):
	signal1 = eeg[i_chn, :, :]
	for j_chn in range(n_chns):		
		signal2 = eeg[j_chn, :,:]
		PLV[i_chn, j_chn,:] = PhaseLockingValue(np.transpose(signal1), np.transpose(signal2))
		del signal2
	del signal1
for i_time in range(n_times):
	np.fill_diagonal(PLV[:,:,i_time], 0)
savemat('matrixConn_PLV.mat',{'PLV_matrix':PLV})

# ciPLV value
ciPLV = np.zeros((n_chns,n_chns, n_times)) # PLV: n_chns * n_chns * n_times
for i_chn in range(n_chns):
	signal1 = eeg[i_chn, :, :]
	for j_chn in range(n_chns):		
		signal2 = eeg[j_chn, :,:]
		ciPLV[i_chn, j_chn,:] = ciPhaseLockingValue(np.transpose(signal1), np.transpose(signal2))
		del signal2
	del signal1
for i_time in range(n_times):
	np.fill_diagonal(ciPLV[:,:,i_time], 0)
savemat('matrixConn_ciPLV.mat',{'ciPLV_matrix':ciPLV})
del ciPLV
