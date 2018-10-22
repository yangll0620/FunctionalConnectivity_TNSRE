import os
import numpy as np
import pandas as pd
import scipy.io as spio
import matplotlib.pyplot as matplot
import comty_utils as utils

wd_code, wd_prep, wd_vis = utils.initEnv('home')
tasklab = ['U', 'V', 'W', 'X']
task = 0

ntimes = 900
nbchan = 64
eigap = -5

fnlabel = pd.Series(['PLVmatrix', 'parPLVmatrix', 
                     'parPLVmatrix_direct', 
                     'parPLVmatrix_direct_trim'])
fnpath = fnlabel.apply(lambda x: '{}/{}/{}'.format(wd_prep, x, tasklab[task]))
fnlist = os.listdir(fnpath[0])

for f in range(len(fnlabel)):
    savepath = utils.checkPath(os.path.join(wd_prep, 
                                            'anoFeat_2dSVD'))
    errtrace = np.zeros((len(fnlist), ntimes))
    
    for i in range(len(fnlist)):
        filepath = os.path.normpath(os.path.join(fnpath[f], fnlist[i]))
        conn = spio.loadmat(filepath)
        keys = list(conn.keys())
        keys = keys[len(keys)-1]
        conn = conn[keys]
        
        connmean = np.mean(conn, axis = 2)
        connmean = connmean[:,:,np.newaxis]
        connmean = np.tile(connmean, (1,1,ntimes))
        
        conn = conn - connmean
        F = np.zeros((nbchan, nbchan))
        for t in range(ntimes):
            F = F + conn[:,:,t] * conn[:,:,t]
        u,s,vh = np.linalg.svd(F, full_matrices = False)
        
        diff = np.zeros(np.int8(nbchan / 2))
        for k in range(np.int8(nbchan / 2)):
            reF = np.dot(u[:,:k], np.dot(np.diag(s[:k]),vh[:k,:]))
            diff[k] = np.linalg.norm(F-reF,ord=2)
        
        k = np.sum(np.diff(diff) < eigap)
        ut = u[:,:k]
        ut2 = np.dot(ut, np.transpose(ut))
        vht = vh[:k,:]
        vht2 = np.dot(np.transpose(vht), vht)

        for t in range(ntimes):
            temp = conn[:,:,t]
            reConn = np.dot(ut2, np.dot(temp, vht2))
            errtrace[i,t] = np.linalg.norm(temp-reConn, ord = np.inf) / np.linalg.norm(temp, ord = np.inf)
        
    np.savetxt(os.path.join(savepath, 'anoFeat_2dSVD_' + fnlabel[f] + '.csv'), 
               errtrace, delimiter = ',')