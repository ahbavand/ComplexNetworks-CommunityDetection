import numpy as np
import igraph as ig
from scipy import spatial


from matplotlib import pyplot as plt
from matplotlib.pyplot import cm


def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data


def create_graph(data):
    edge_list=[]
    for i in range(0,len(data)):
        e = int(data[i][0])
        w = int(data[i][1])
        edge_list.append([e,w])
    g=ig.Graph(10000,edge_list)
    zeronodedegree=[]
    for i in range(0,10000):
        if(g.vs.degree()[i]==0):
            zeronodedegree.append(i)
    g.delete_vertices(zeronodedegree)
    return g

data=convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/1.txt')
g=create_graph(data)


def calculate_betweenness_clustring_coefficient(g):
    #    betw=g.betweenness()
    #    sum_betweenness=0
    #    for i in range(0,len(betw)):
    #        sum_betweenness=sum_betweenness+betw[i]
    betweenness_edge = g.edge_betweenness(directed=True)
    sum_betweenness = 0
    for i in range(0, len(betweenness_edge)):
        sum_betweenness = sum_betweenness + betweenness_edge[i]
    avg_betweenness = sum_betweenness / len(betweenness_edge)
    print(avg_betweenness)
    print(g.transitivity_undirected())



calculate_betweenness_clustring_coefficient(g)







