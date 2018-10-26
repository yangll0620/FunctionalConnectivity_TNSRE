# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-10-25 15:46:36
# @Last Modified by:   yll
# @Last Modified time: 2018-10-25 15:59:52

import numpy as np

# calculate the reconstruction similarity of two matrices
# input: recon_M: reconstructed matrix
#		 orignal_M: original matrix
def recon_similarity(recon_M, orignal_M):
	recon_sim = np.float(np.linalg.norm(orignal_M-recon_M, ord = np.inf)) / np.float(np.linalg.norm(orignal_M, ord = np.inf))
	return recon_sim

# calculate the reconstruction similarity of two 3D tensor: n_chns * n_chns * n_times
# input: recon_tensor: reconstructed connective matrix along time
#		 orignal_M: original connective matrix along time
def recon_similarity_allTime(recon_tensor, orignal_tensor):
	n_times= recon_tensor.shape[2]
	recon_sim_allTime = np.zeros((n_times))
	for i_time in range(n_times):
		recon_M = recon_tensor[:,:,i_time]
		orignal_M = orignal_tensor[:,:,i_time]
		recon_sim_allTime[i_time]  = recon_similarity(recon_M, orignal_M)
		del orignal_M, recon_M
	return recon_sim_allTime