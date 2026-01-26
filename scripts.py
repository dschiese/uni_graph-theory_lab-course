from synkit.IO import rsmi_to_its
from synkit.Vis import GraphVisualizer
import matplotlib.pyplot as plt
import random
import pandas as pd

# Visualizes and prints the ITS graph for a given reaction SMILES
def plot_and_print_its_graphs(rsmi:str):
  full_graph = rsmi_to_its(rsmi, core=False)

  print("ITS graph")
  for n, d in full_graph.nodes(data=True):
     print(f"n: {n},d: {d}")
  for u,v, d in full_graph.edges(data=True):
      print(u,v, d)

  # Visualize ITS
  try:
    viz = GraphVisualizer()
    fig = viz.visualize_its(full_graph, use_edge_color=True)
    plt.show()
  except Exception as e:
    print(f"Visualization failed: {e}")

# Takes a random sample of classes and reactions per class from the dataset
# If classes and/or reactions_per_class is not specified, they are chosen randomly within reasonable bounds
# Args:
#   df: DataFrame containing the dataset with a 'rxn_class' column
#   classes: Number of unique reaction classes to sample
#   reactions_per_class: Number of reactions to sample per class
# Returns:

def create_varied_set(data, chosen_classes:list, reactions_per_class:int) -> pd.DataFrame:
    varied_set = pd.DataFrame() # Return as array of DataFrames to concatenate later

    for cls in chosen_classes:
        if not reactions_per_class:
            reactions_per_class = random.randint(20, 200)
        class_subset = data[data['rxn_class'] == cls].sample(n=reactions_per_class)
        varied_set = pd.concat([varied_set, class_subset])

    return varied_set.reset_index(drop=True)