import numpy as np
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import sys

arr = np.array([
	[1,2,3],
	[0,1,2],
	[3,0,5],
	[4,1,3],
	[5,0,1]
	])

cen_0 = np.array([1,0,0])
cen_1 = np.array([0,1,1])

def dist(p1, p2):
	return p1 - p2

cluster_0 = np.array([],dtype=np.float64).reshape(0,3)
cluster_1 = np.array([],dtype=np.float64).reshape(0,3)

clust_0_avg = None
clust_1_avg = None

cluster_0_init = False
cluster_1_init = False

for i in range(0,15):

	print("Iteration {}".format(i))
	print("Centroid 1: {}".format(cen_0))
	print("Centroid 2: {}".format(cen_1))
	print("Cluster 0: \n{}\n".format(cluster_0))
	print("Cluster 1: \n{}\n\n".format(cluster_1))

	cluster_0 = np.array([],dtype=np.float64).reshape(0,3)
	cluster_1 = np.array([],dtype=np.float64).reshape(0,3)

	clust_0_avg = None
	clust_1_avg = None

	for p in arr:
		dst_0 = np.sum(np.absolute(dist(p, cen_0)))
		dst_1 = np.sum(np.absolute(dist(p, cen_1)))

		if(dst_0 < dst_1):
			cluster_0 = np.vstack((cluster_0, p))
		else:
			cluster_1 = np.vstack((cluster_1, p))

	clust_0_avg = np.add.reduce(cluster_0) / len(cluster_0)
	clust_1_avg = np.add.reduce(cluster_1) / len(cluster_1)

	cen_0 = np.round(clust_0_avg, 3)
	cen_1 = np.round(clust_1_avg, 3)




















