#------------Plotting and Determinig of Centralities-----------------------
import numpy as np
import networkx as nx
import pylab as plt
from operator import itemgetter
from networkx.algorithms import bipartite
import sys
sys.stdout = open("output.txt", "w")

H=nx.read_weighted_edgelist('list.weighted12.12.14.1.edgelist')
nx.draw_networkx(H,node_size=1500,font_size=10)
#nx.draw_spring(H)

plt.show()


a=H.number_of_nodes()
s='The no of nodes: ' +repr(a)
print s

a= H.number_of_edges()
s='The no of edges: ' +repr(a)
print s

#a=  H.edges()
#s= 'The Edges : ' +repr(a)
#print s

a= H.degree()
s='The Degree:' +repr(a)
print s

#a=H.adjacency_list()
#s='The Adjacency List:'+repr(a)
#print s

deg=nx.degree(H)


a= min(deg.values())
s='The min degree: ' +repr(a)
print s


a = max(deg.values())
s='The max degree: ' +repr(a)
print s

a = nx.is_connected(H)
s='Is a connected graph: ' +repr(a)
print s

a= H.is_multigraph()
s='Is a multgraph: ' +repr(a)
print s

cl = list( nx.find_cliques(H) )
s= 'list of cliques :'
print s
print cl


#calculate the centrality measures

cc=nx.closeness_centrality(H)
s='sorted closeness centrality:'
print s
print sorted(cc.items(), key=itemgetter(1), reverse=True)

dc=nx.degree_centrality(H)
s='sorted degree centrality:'
print s
print sorted(dc.items(), key=itemgetter(1), reverse=True)


bc = nx.betweenness_centrality(H)
s='sorted between ness centrality:'
print s
print sorted(bc.items(), key=itemgetter(1), reverse=True)

pr=nx.pagerank(H)
s='Page Rank sorted:'
print s
print sorted(pr.items(), key=itemgetter(1), reverse=True)

s='sorted eigenvector centrality:'
print s
ec = nx.eigenvector_centrality(H)
print sorted(ec.items(), key=itemgetter(1), reverse=True)


nx.write_gml(H,"test1.gml")
print "------------Important people List-----------------"


