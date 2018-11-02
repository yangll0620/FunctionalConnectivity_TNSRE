# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-02 10:37:25
# @Last Modified by:   yll
# @Last Modified time: 2018-11-02 10:50:54

import numpy as np
from igraph import Graph
def community_detection(matrix_conn):
	""" detect community based on the connectivity matrix matrix_connectivity

	@ param matrix_conn : connectivity matrix

	@ return membership : a vector indicating the community index for each vertex i.e. [0,0,0,1,1,1,0,0,2,2])
	"""
	np.fill_diagonal(matrix_conn, 0) # no connective for vertex itself
	g_conn = Graph().Adjacency((matrix_conn >0).tolist(), mode = 'UNDIRECTED')
	g_conn.es['weight'] = matrix_conn[matrix_conn.nonzero()]
	comty_VertexClustering = g_conn.community_fastgreedy(weights='weight').as_clustering()
	membership = comty_VertexClustering.membership  # membership: indicating the community index for each vertex i.e. [0,0,0,1,1,1,0,0,2,2]

	return membership
