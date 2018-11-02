# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-02 10:55:38
# @Last Modified by:   yll
# @Last Modified time: 2018-11-02 11:33:55

from igraph import Graph
from igraph import ClusterColoringPalette
from igraph import Layout
from igraph import plot

def network_visualization(w_plot, membership, name, coord_xy):
	"""
	plot the newwork

	@ param w_plot: weight matrix for plotting

	@ param membership: a vector indicating the community index for each vertex i.e. [0,0,0,1,1,1,0,0,2,2])

	@ param name: vertex name vectors

	@ param coord_xy: x and y coordinates in a planar for vertices (n_vertices * 2)

	"""
	# construct the plot graph
	g_plot = Graph().Adjacency((w_plot > 0).tolist(), mode = 'UNDIRECTED')
	n_clusters = len(set(membership))
	n_vertics = len(g_plot.vs)
	n_edges = len(g_plot.es)

	# set the attributes for vertices and edges
	g_plot.vs['name'] = name
	g_plot.vs['i_cluster'] = membership # the cluster index for each vertex
	g_plot.es['weight'] = w_plot
	# assign the cluster index for each edge
	for v1, v2 in g_plot.get_edgelist():
		eid = g_plot.get_eid(v1,v2)
		if membership[v1] != membership[v2]:
			g_plot.es[eid]['i_cluster'] = n_clusters #if v1,v2 belong to different clusters, g_plot.es['i_cluster'] = n_cluster, crossing clusters condition
		else:
			g_plot.es[eid]['i_cluster'] = membership[v1] # if v1,v2 belong to the same cluster i, g_plot.es['i_cluster'] = i

	palette = ClusterColoringPalette(n=n_clusters+1) # set one palette for each cluster, extra one color for the crossing edge
	vertex_color_list = [palette.get(g_plot.vs[i]['i_cluster']) for i in range(n_vertics)]# configure the vertex color
	edge_color_list = [palette.get(g_plot.es[i]['i_cluster'])  for i in range(n_edges)] # configure the edge color

	visual_style = {}
	layout = Layout(list(coord_xy))
	layout.mirror(1)
	visual_style["layout"] = layout
	visual_style["vertex_label"] = g_plot.vs["name"]
	visual_style["vertex_color"] = vertex_color_list
	visual_style["edge_color"] = edge_color_list
	#visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]

	plot(g_plot, **visual_style)
