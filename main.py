import networkx as nx
import matplotlib.pyplot as plt

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

G_2=nx.DiGraph()
G_2.add_edges_from([(1,3),(3,2),(2,1),(4,1),(4,2),(4,12),(3,5),(5,6),(5,8)
,(6,7),(6,8),(6,10),(8,9),(8,10),(10,9),(10,11),(9,11),(11,12)])

nx.draw(G_2)


G_3 = nx.Graph()
G_3.add_edge('A','B',weight=22)
G_3.add_edge('B','H',weight=34)
G_3.add_edge('H','I',weight=19)
G_3.add_edge('I','D',weight=30)
G_3.add_edge('D','A',weight=12)
G_3.add_edge('A','C',weight=9)
G_3.add_edge('A','B',weight=22)
G_3.add_edge('C','B',weight=35)
G_3.add_edge('A','D',weight=12)
G_3.add_edge('B','F',weight=36)
G_3.add_edge('C','F',weight=42)
G_3.add_edge('C','E',weight=65)
G_3.add_edge('C','D',weight=4)
G_3.add_edge('D','E',weight=33)
G_3.add_edge('H','F',weight=24)
G_3.add_edge('H','G',weight=25)
G_3.add_edge('I','G',weight=21)
G_3.add_edge('G','E',weight=23)
G_3.add_edge('E','F',weight=18)

nx.draw(G_3)