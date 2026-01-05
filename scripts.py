from synkit.IO import rsmi_to_its, rsmi_to_graph
from synkit.Vis import GraphVisualizer
import matplotlib.pyplot as plt
import networkx as nx

def plot_and_print_its_graphs(rsmi:str):
  full_graph = rsmi_to_its(rsmi, core=False)

  print("ITS graph")
  for n, d in full_graph.nodes(data=True):
      print(n, d)
  for u,v, d in full_graph.edges(data=True):
      print(u,v, d)

  # Visualize ITS
  viz = GraphVisualizer()
  fig = viz.visualize_its(full_graph, use_edge_color=True)
  plt.show()
