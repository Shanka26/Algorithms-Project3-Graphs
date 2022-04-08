import networkx as nx
import matplotlib as plt

G = nx.Graph()
G.add_edge('A','B')
G.add_edge('A','F')
G.add_edge('A','E')

G.add_edge('B','F')
G.add_edge('B','C')

G.add_edge('C','D')
G.add_edge('C','G')
G.add_edge('D','G')

G.add_edge('E','F')
G.add_edge('E','I')

G.add_edge('I','J')
G.add_edge('G','J')

G.add_edge('I','M')
G.add_edge('M','N')

G.add_edge('H','L')
G.add_edge('H','K')

G.add_edge('K','L')
G.add_edge('L','P')
G.add_edge('K','O')

nx.draw(G)
