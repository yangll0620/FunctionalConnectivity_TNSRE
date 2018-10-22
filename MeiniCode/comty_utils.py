import numpy as np
import os
import jgraph as ig

def checkPath(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def checkSymmetric(w, diagfill = 0, tol = 1e-8):
    flag = np.allclose(w, w.T, atol = tol)
    if not flag:
        w *= np.tri(*w.shape)
        w = w + w.T
    np.fill_diagonal(w, diagfill)
    return (flag, w)

def create_graph(w, selfloop = False, directed = False):
    flag, w = checkSymmetric(w, diagfill = selfloop)
    g = ig.Graph.Adjacency((w>0).tolist())
    
    if not directed:
        g = g.as_undirected()
        
    g.es['weight'] = w[w.nonzero()]
    g.es['width'] = w[w.nonzero()]
    return (g, w)

def find_comty(g, method):
    if method == 'louvain':
        comty = g.community_multilevel(g.es['weight'],False)
    elif method == 'infomap':
        comty = g.community_infomap(g.es['weight'])
    elif method == 'labelProp':
        comty = g.community_label_propagation(g.es['weight'])
    elif method == 'edgeBetween':
        comty = g.community_edge_betweenness(None,False,g.es['weight'])
        comty = comty.as_clustering()
    elif method == 'spinglass':
        comty = g.community_spinglass(g.es['weight'])
    elif method == 'walktrap':
    	comty = g.community_walktrap(g.es['weight'])
    elif method == 'eigenvector':
    	comty = g.community_leading_eigenvector(None, g.es['weight'])
    elif method == 'modularity':
    	comty = g.community_optimal_modularity(g.es['weight'])
        
    nclust = len(comty.sizes())
    mod = comty.modularity
    clustIdx = comty.membership
    return (clustIdx, nclust, mod)
        