# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-10-22 15:16:46
# @Last Modified by:   yll
# @Last Modified time: 2018-10-25 16:11:28

import numpy as np

# ref: Chris Ding (2004), 2-Dimensional Singular Value Decomposition for 2D Maps and Images
# based on Meini'code: anoFeat_2dSVD.py
# low-rank approximation of a series of matrics using 2DSVD along the third dimension
# input: a 3D connectivity tensor: n_chn * n_chn *n_times 
def conn_matrix_lowRankApprox_2DSVD_Chris(conn_tensor):

	# calculate variance matrix, variance matrix is positive semidefinite matrix
	conn_matrix_mean = np.mean(conn_tensor, axis = 2) # conn_matrix_mean: n_chn * n_chn, symmetric matrix
	# row-row variance matrix = column-column variance matrix for symmetrix matrix
	n_chn,n_chn, n_times = conn_tensor.shape
	var_matrix_sum = np.zeros((n_chn, n_chn)) 
	for i in range(n_times):
		matrix = conn_tensor[:,:,i] # matrix.shape = (n_chn,n_chn)
		var_matrix_sum = var_matrix_sum + (matrix - conn_matrix_mean) * np.transpose(matrix- conn_matrix_mean)
		del matrix
	var_matrix = var_matrix_sum / np.int8(n_times)
	del var_matrix_sum
	
	# Singular value decompsition of variance matrix: var_matrix
	# for positive semidefinite normal matrix, svd = eignvalue decomposition
	u,s,vh = np.linalg.svd(var_matrix, full_matrices = False)

	# select the value of k 
	# using the differences between reconstructed and orignal variance matrix
	eigap = 5 # the same value as meini
	diff = np.zeros(np.int8(n_chn /2))
	for k in range(np.int8(n_chn/2)):
		re_var_matrix = np.dot(u[:,:k], np.dot(np.diag(s[:k]),vh[:k,:]))
		diff[k] = np.linalg.norm(var_matrix - re_var_matrix,ord=2)
	k = np.sum(np.diff(diff) < eigap)

	# reconstruct approximated matrix
	u_k = u[:,:k]
	u_k2 = np.dot(u_k, np.transpose(u_k))
	vh_k = vh[:k,:]
	vh_k2 = np.dot(np.transpose(vh_k), vh_k)
	re_conn_matrix = np.zeros(conn_tensor.shape) 
	for i in range(n_times):
		matrix = conn_tensor[:,:,i]
		re_conn_matrix[:,:,i] = np.dot(u_k2, np.dot(matrix, vh_k2))
		del matrix

	return re_conn_matrix
