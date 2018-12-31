import numpy as np
import networkx as nx
import operator
from networkx.algorithms import community
community.modularity()



def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data

def create_graph(data):
    g = nx.DiGraph()
    for i in range(0,len(data)):
        e = int(data[i][0])
        w = int(data[i][1])
        g.add_edge(e, w)
    return g



data=convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/1.txt')
g=create_graph(data)

#google_page_rank=nx.pagerank(g, alpha=0.85)
#print(google_page_rank)
#sorted_x = sorted(google_page_rank.items(), key=operator.itemgetter(1))
#print(sorted_x)

hubs,authorities=nx.hits(g)

dict={}
for key, value in hubs.items():
    dict[key]=hubs[key]+authorities[key]


sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
#print(hubs)
#print(authorities)
print(sorted_x)