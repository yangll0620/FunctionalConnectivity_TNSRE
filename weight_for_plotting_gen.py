# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-02 11:35:51
# @Last Modified by:   yll
# @Last Modified time: 2018-11-02 12:06:25

from scipy import stats
import numpy as np
def weight_for_plotting_gen(matrix_conn, p_sig):
	"""
	generate new connective matrix for just showing the most significant edges with p = p_sig

	@ param matrix_conn : connectivity matrix

	@ param p_sig: significant level

	@ return w_plot: the generated connective matrix for plotting

	"""
	
	shape, loc, scale = stats.lognorm.fit(matrix_conn.flatten()) # fit a lognorm distribution for all the connectivity weights 
	pval = stats.lognorm.cdf(matrix_conn.flatten(order='c'), s=shape, loc=loc, scale=scale) # Cumulative distribution function. pval: (n_chns*n_chns,)
	pval = np.reshape(pval, matrix_conn.shape, order='c') # pval: (n_chns,n_chns)
	w_plot = matrix_conn * (pval>p_sig).astype(float) # w_plot: the weights of significant edges remains, the weights of the insignificant edges = 0

	return w_plot