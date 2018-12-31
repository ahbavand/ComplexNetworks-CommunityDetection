import numpy as np
import networkx as nx
import operator
from networkx.algorithms import community
from sklearn.cluster import KMeans

def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data


def create_graph(data):
    g = nx.Graph()
    for i in range(0,len(data)):
        e = int(data[i][0])
        w = int(data[i][1])
        g.add_edge(e, w)
    return g



data=convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/1.txt')
g=create_graph(data)



a=nx.laplacian_matrix(g)
a=a.todense()

kco=Y[:,[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26]]
kmeans =KMeans(n_clusters=100, random_state=0).fit(kco)
labels=kmeans.labels_


p={}
node_label=g.nodes()
i=0
for node in node_label:
    p[node]=labels[i]
    i=i+1


min_cut = 0
for edge in g.edges():
    if p[edge[0]] != p[edge[1]]:
        min_cut += 1

print(min_cut)