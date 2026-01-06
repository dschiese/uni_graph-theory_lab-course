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
def create_varied_set(df: pd.DataFrame, classes:int, reactions_per_class:int) -> pd.DataFrame:
    class_counts = df['rxn_class'].value_counts()
    selected_classes = random.sample(list(class_counts.index), classes)
    varied_set = pd.DataFrame()

    for cls in selected_classes:
        if not reactions_per_class:
            reactions_per_class = random.randint(20, 200)
        class_subset = df[df['rxn_class'] == cls].sample(n=reactions_per_class, random_state=42)
        varied_set = pd.concat([varied_set, class_subset])

    return varied_set.reset_index(drop=True)