# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-02 11:51:12
# @Last Modified by:   yll
# @Last Modified time: 2018-11-08 15:34:16

import numpy as np
from tensorly.decomposition import tucker
from tensorly.tucker_tensor import tucker_to_tensor
from numpy.linalg import svd

def representive_connMatrix_SVD(conn_seg):
	""" extract one representive connectivity matrix from a series of connective matrices for each time segment
		based on SVD decomposition

		@ parameter conn_seg: a series of connective matrics for a time segment (n_chns * n_chns * n_times)

		return conn_repre: one representive connective matrix for this time segment
	"""
	n_chns, n_chns, n_times = conn_seg.shape

	''' SVD decomposition for the connectivity matrix in each time i_time'''
	Us = np.zeros((n_chns, n_chns, n_times))
	VHs = np.zeros((n_chns, n_chns, n_times))
	Ss = np.zeros((n_chns, n_times))
	for i_time in range(n_times):
		matrix_conEach = conn_seg[:,:,i_time] # matrix_conEach: the connectivity matrix in each time i
		u,s,vh = svd(matrix_conEach, full_matrices = True) # matrix_conEach = u * s * vh
		Us[:,:,i_time], Ss[:,i_time], VHs[:,:,i_time]= u, s, vh
		del matrix_conEach, u, s, vh

	n_comp = Ss.shape[0]

	''' find the largest k so that the variance > signlev'''
	signlev = 0.85
	S_sumrep = np.tile(np.sum(Ss, axis = 0),(n_chns,1))
	S_cumscale = np.cumsum(Ss,axis=0)/S_sumrep 
	S_cumscaleMean = np.mean(S_cumscale,axis = 1)
	k = np.nonzero(S_cumscaleMean>signlev)[0][0]

	''' using the first k vectors to reconstruct the each matrix'''
	U_mean = np.mean(Us[:,0:k+1,:],axis = 2) # column vectors
	VH_mean = np.mean(VHs[0:k+1,:,],axis = 2) # row vectors
	Ss_k = Ss[0:k+1,:]
	recon_conn_seg = np.zeros(conn_seg.shape)
	for i_time in range(n_times):
		s = Ss_k[:,i_time]
		recon_conn_seg[:,:,i_time] = np.dot(U_mean * s, VH_mean)
		del s

	''' average the recontructed matrices to obtain the representive matrix'''
	conn_repre =  np.mean(recon_conn_seg, axis=2)
	return conn_repre


def representive_connMatrix_tucker(conn_seg):
	""" extract one representive connectivity matrix from a series of connective matrices for each time segment
		based on Tucker decomposition

		@ parameter conn_seg: a series of connective matrics for a time segment (n_chns * n_chns * n_times)

		return conn_repre: one representive connective matrix for this time segment

	"""
	rank = [15,15,3]
	core, factors = tucker(conn_seg, ranks=rank)
	recon_conn_seg = tucker_to_tensor(core, factors) # recon_conn_seg: 64*64*60
	conn_repre =  np.mean(recon_conn_seg, axis=2) # conn_repre: n_chns * n_chns, connective matrix summary for each segment

	return conn_repre