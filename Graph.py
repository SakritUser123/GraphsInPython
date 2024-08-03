import sys
import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

nodes = range(1,7)
edges = [(1,2),(2,3),(1,3),(1,4),(2,4),(3,4),(1,6),(3,5)]
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)
draw_params = {
	'with_labels': True,
    'node_color': 'orange',
    'node_size': 700,'width':2,
    'font_size': 14,
    'pos': nx.layout.spring_layout(graph,seed=1)
    }
nx.draw(graph, **draw_params)
plt.show()
