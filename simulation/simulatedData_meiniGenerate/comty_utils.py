import numpy as np
import os
import igraph as ig
import igraph.drawing.colors as palettes
import h5py
import scipy.io as spio


def initEnv():
    dir_prep = 'C:/Users/meini/OneDrive/eegAnalysis'
    dir_code = 'C:/Respository/eeganalysis'
    dir_vis = 'C:/Users/meini/OneDrive/eegAnalysis/visualization'
    
    return dir_code, dir_prep, dir_vis


def checkPath(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def loadmat(filename, matname):
    try:
        conn = spio.loadmat(filename)
        conn = conn[matname]
    except NotImplementedError:
        with h5py.File(filename,'r') as file:
            conn = np.array(file[matname])
    
    return conn
                


def checkSymmetric(w, diagfill=0, tol=1e-8):
    def checkSymmetric2D(w_sin, diagfill=0, tol=1e-8):
        flag = np.allclose(w_sin, w_sin.transpose(), atol=tol)
        if not flag:
            w_sin *= np.tri(*w_sin.shape)
            w_sin = w_sin + w_sin.T
            np.fill_diagonal(w_sin, diagfill)
        return flag, w_sin

    flag = True
    if len(w.shape) > 2:
        for i in range(w.shape[2]):
            flag_sin, w[:, :, i] = checkSymmetric2D(w[:, :, i], diagfill=diagfill, tol=tol)
            if not flag_sin:
                flag = flag_sin
    else:
        flag, w = checkSymmetric2D(w, diagfill=diagfill, tol=tol)

    return flag, w


def rescale_minmax(data, min_scale=0, int_len=1):
    data -= np.min(np.array(data).flatten())
    data /= (np.max(data.flatten()) - np.min(data.flatten()))

    data += min_scale
    data *= int_len
    return data


def create_graph(w, labels=None, selfloop=False, directed=False, rescale=True, lowbnd=0, wmin=0, wlen=1):
    w = np.multiply(w, w>lowbnd)
    if rescale:
        w = rescale_minmax(w, min_scale=wmin, int_len=wlen)
    flag, w = checkSymmetric(w, diagfill=selfloop)
    
    g = ig.Graph.Adjacency((w>0).tolist())
    if not directed:
        g = g.as_undirected()
        wght = w * np.tri(*w.shape)
    else:
        wght = w
    
    g.es['weight'] = wght[wght.nonzero()]
    g.es['width'] = wght[wght.nonzero()]
    
    if labels is not None:
        g.vs['name'] = labels
        g.vs['label'] = labels

    return g, w


def graph_style(g, layout, labels=None):
    visual_style = dict()
    visual_style['vertex_color'] = 'black'
    visual_style['vertex_label_size'] = 10
    visual_style['vertex_label_dist'] = 2
    visual_style['vertex_label_color'] = 'black'
    try:
        visual_style['vertex_label'] = g.vs['label']
    except KeyError:
        if labels is not None:
            if type(labels) is np.ndarray:
                labels = labels.tolist()
            
            visual_style['vertex_label'] = labels
            
    visual_style['edge_width'] = g.es['weight']
    visual_style['layout'] = layout
    outdegree = g.outdegree()
    visual_style["vertex_size"] = [x/max(outdegree)*10+5 for x in outdegree]
    
    return visual_style    


def find_comty(g, method):
    if method == 'fastgreedy': # *****
        comty = g.community_fastgreedy(weights='weight')
        comty = comty.as_clustering()
    elif method == 'leading_eigenvector': # *****
        comty = g.community_leading_eigenvector(weights='weight')
    elif method == 'multilevel':
        comty = g.community_multilevel(weights='weight')
    elif method == 'spinglass':
        comty = g.community_spinglass(weights='weight')
    else:
        print('Invalid method.')

    membership = comty.membership
    return membership


def graph_plot(g, layout, clustering=None, savename = 'network.png'):
    visual_style = graph_style(g,layout)
    if clustering is not None:
        cluster_idx = find_comty(g,clustering)
        palette = palettes.ClusterColoringPalette(len(np.unique(cluster_idx)))
        g.vs['color'] = [palette[cluster_idx[x]] for x in range(len(cluster_idx))]
        visual_style['vertex_color'] = g.vs['color']
    else:
        visual_style['vertex_color'] = 'black' 
    
    visual_style['bbox'] = [500, 500]     
    visual_style['margin'] = np.array([10,10,10,30]).tolist()  
    return ig.plot(g,savename ,**visual_style)