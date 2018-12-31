import networkx as nx
import numpy as np
import scipy.cluster.vq as clustering





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

def create_clusters(graph):
    old_modularity = -1
    new_modularity = 1
    labels = []
    node_list = {}
    node_index = []
    node_cluster = {}
    while new_modularity >= old_modularity:
        if len(labels) == 0:
            new_labels = create_two_clusters(graph)
            if len(labels) == 0:
                labels = new_labels
                node_list, node_index, node_cluster = get_nodes(graph, labels)
            old_modularity = compute_modularity(node_cluster, graph)
            print(old_modularity)
        else:
            new_modularity = old_modularity
            node_list, node_index, fake_value = get_nodes(graph, labels)
            num_of_clusters = range(len(node_list))
            index = 0
            for key in num_of_clusters:
                print(index)
                subgraph = graph.subgraph(node_index[key])
                new_labels = create_two_clusters(subgraph)
                fake_val, fake_val2, node_cluster_local = get_nodes(subgraph, new_labels)
                node_cluster, labels = update_labels(node_cluster, node_cluster_local,)
                index=index+1
            old_modularity = new_modularity
            new_modularity = compute_modularity(node_cluster, graph)
            print(new_modularity)









def update_labels(node_cluster_total, node_cluster_local, key, max_cluster_number):
    for node in node_cluster_local:
        if node_cluster_local[node] == 1:
            node_cluster_total[node] = max_cluster_number
    sorted_node_cluster = sorted(node_cluster_total)
    new_labels = []
    for key in node_cluster_total:
        new_labels.append(node_cluster_total[key])
    return (node_cluster_total, new_labels)





def create_two_clusters(graph):
    nodes = sorted(graph.nodes())
    modularity_matrix = nx.modularity_matrix(graph, nodes)
    eigenvalues, eigenvectors = np.linalg.eigh(modularity_matrix)
    clusters, centroids = clustering.kmeans(eigenvectors[-2:].getT(), 2)
    labels, dist = clustering.vq(eigenvectors[0:2].getT(), clusters)
    return labels


def compute_modularity(clustering_labels, graph):
    print("salam")
#    return community_louvain.modularity(clustering_labels, graph)

def get_nodes(graph, labels):
    node_list = {}
    node_index = {}
    node_cluster = {}
    nodes = sorted(graph.nodes())
    index = 0
    for node in nodes:
        node_cluster[node] = labels[index]
        if labels[index] in node_index:
            node_index[labels[index]].append(node)
        else:
            node_index[labels[index]] = [node]
        if labels[index] in node_list:
            node_list[labels[index]].append(index)
        else:
            node_list[labels[index]] = [index]
        index += 1
        return (node_list, node_index, node_cluster)









data=convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW1/1.txt')
g=create_graph(data)
























