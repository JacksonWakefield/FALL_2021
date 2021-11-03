import networkx as nx
import matplotlib.pyplot as plt
import json


G = nx.Graph()

data = {}

with open("Redditors_JSON.json") as dataFile:
    
    data = json.load(dataFile)

#Minimum of 3 comments
minimumToGraph = 5

for elem in data:
    
    data_individual = data[elem]
    
    for key in data_individual:
        value = data_individual[key]
        
        if(value >= minimumToGraph):
            G.add_edge(elem, key)

##### NETWORK GRAPHING #####
#
plt.figure(1, figsize=(12, 8))
nx.draw(G, with_labels=True, font_weight='bold', font_size = 8, node_size = 20)


##### HISTORGRAM GRAPHING - DEGREE DISTRIBUTION #####

#degrees = [G.degree(n) for n in G.nodes()]
#
#plt.xlabel("Degree of nodes")
#plt.ylabel("Number of nodes")
#
#plt.hist(degrees)
#
#plt.show()

##### PAGE RANK  #####

#pagerank = nx.pagerank(G)
#
#for key in pagerank:
#    if(pagerank[key] > 0.005):
#        print(key + ": " + str(pagerank[key]))
            
##### PAGE RANK  #####

#centrality = nx.betweenness_centrality(G)
#
#for key in centrality:
#    if(centrality[key] > 0.05):
#        print(key + ": " + str(centrality[key]))