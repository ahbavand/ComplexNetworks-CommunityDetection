import numpy as np
import igraph as ig
from scipy import spatial



def create_graph(data_point,threshold):
    edge_list=[]
    for i in range(0,len(data_point)):
        for j in range(i,len(data_point)):
            if(spatial.distance.cosine(data_point[i],data_point[j])<threshold and i!=j):
                edge_list.append([i,j])
    g=ig.Graph(len(data_point),edge_list)
    return g



def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data

def cluster_NMI_CALC(g):
    from igraph import arpack_options
    arpack_options.maxiter = 300000
    a = g.community_leading_eigenvector()
    print(g.modularity(a))

    real = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/real')
    from sklearn.metrics.cluster import normalized_mutual_info_score
    clusters = np.zeros(len(data))
    for i in range(0, len(data)):
        for j in range(0, len(a)):
            if (i in a[j]):
                clusters[i] = j

    np.savetxt('Q7.csv',clusters)
    print(normalized_mutual_info_score(real, clusters))



data=convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/digits')
g=create_graph(data,0.12)
cluster_NMI_CALC(g)


