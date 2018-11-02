# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-10-31 16:13:41
# @Last Modified by:   yll
# @Last Modified time: 2018-11-02 12:08:18

import pandas as pd
import numpy as np
from scipy.io import loadmat

import sys
sys.path.append("../")
from community_detection import community_detection
from network_visualization import network_visualization
from weight_for_plotting_gen import weight_for_plotting_gen
from representive_connMatrix_gen import representive_connMatrix_tucker

'''
	framework for the whole dynamic network analysis on the simulated connectivity matrix
	components:
		1. detect change points (now still in matlab code, successfully detect the two change points 61 and 121)
		2. extract the representive connectivity matrix for each time segment
		3. detect community from the representive connectivity matrix 
		4. network visualization
'''

# load simulated connectivity matrix
data = loadmat('./matrixConn_Surrogate.mat')
matrix_Con_Surr = data['matrix_Con_Surr'] # matrix_Con_Surr: n_chns * n_chns * n_times

# read the channel location informations 
inf_chans = pd.read_csv('acticap64xy.csv', sep=' ', index_col = False, header = None).values # inf_chans: n_chns * 4
idx_name = 0  # inf_chns column 0: the channel index (0,1,2...), column 3: channel names ('FP1' et.al)
name = inf_chans[:,idx_name] 
coord_xy = inf_chans[:,1:3] # coord_xy:n_chans * 2, inf_chans column 1 & 2: x,y coordinates in planar 

# detect change points
''' separate EEG into individal segments'''
conn_seg = matrix_Con_Surr[:,:,0:60] # individual segment

''' extract the representive connectivity matrix for each time segment'''
connM_repre = representive_connMatrix_tucker(conn_seg)
'''detect community'''
membership = community_detection(connM_repre)
'''Network Visualization '''
# generate new connective matrix for just showing the most significant edges with p = p_sig
p_sig = 0.95
w_plot = weight_for_plotting_gen(connM_repre, p_sig)
# visualize the network
network_visualization(w_plot, membership, name, coord_xy)

