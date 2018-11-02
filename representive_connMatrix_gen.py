# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-02 11:51:12
# @Last Modified by:   yll
# @Last Modified time: 2018-11-02 12:04:28

import numpy as np
from tensorly.decomposition import tucker
from tensorly.tucker_tensor import tucker_to_tensor

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