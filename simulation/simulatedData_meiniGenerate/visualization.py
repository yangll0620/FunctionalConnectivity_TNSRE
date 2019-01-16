# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:22:48 2018

@author: welkin
"""

import os, time, random, sys
import matplotlib
#matplotlib.use("GTK3Cairo")
import matplotlib.pyplot as pyplot
import numpy as np
import igraph as ig
import comty_utils as comty
from igraph import plot

def main():
      
    #---------------------------------------------------------------------#
    # Layout for simulated EEG
    idx,x,y,label = np.loadtxt('acticap64xy.csv',
                        dtype={'names':('idx','x','y','label'),
                               'formats':('i','f','f','U3')},
                        delimiter=' ',unpack=True)
    loc = np.stack([x, y],axis=-1).tolist()
    layout = ig.Layout(loc)
    layout.mirror(1)
    
    # simulated connection
    prefix = 'sim_chaos_colpitts_p64_'
    suffix = '.mat'
    filename = ['r6','r6_LF','r6_LF_RP_iid','r6_LF+RP',
                'r4_3r_iid','r4_3r_2inter','r4_3r_3inter','r12']
    matname = 'conn_nt'
    
    for fname in filename:
        conn = comty.loadmat(os.path.join(prefix+fname+suffix),matname)
        conn_tmp = np.mean(conn,2)
        g,w = comty.create_graph(conn_tmp,labels=label,rescale=False,lowbnd=0)
        comty.graph_plot(g,layout,clustering = 'fastgreedy', savename = fname + '.png')
        
    #---------------------------------------------------------------------#
    # Layout for minimal EEG
    loc_min = np.array([[-1,1],[1,1],[2,-1],[0,-1],[-2,-1]]).tolist()
    label_min = np.array(['x1','x2','x3','x4','x5'])
    layout_min = ig.Layout(loc_min)
    

if __name__ == "__main__":
    main()
    