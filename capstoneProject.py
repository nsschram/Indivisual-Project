import csv
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def randomDirectory():
    with open('randDir.csv', 'w', newline='') as csvfile:
        fieldnames = ["x", "y", "weight"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer. writeheader()
        for i in range(10):
            x = str(random.randint(0,100))
            y = str(random.randint(0,100))
            weight = str(random.randint(0,10))
            print(f"x = {x} y = {y} weight = {weight}")
            writer.writerow({'x': x, 'y': y, 'weight': weight})
    pass

def readDir():
    x = []
    y = []
    w = []
    with open('randDir.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(row['x'])
            y.append(row['y'])
            w.append(row['weight'])
    return x, y, w

def connectDots(x, y, w):
    #G = nx.Graph()
    #G.add_edge(1, 2)  # default edge data=1
    #G.add_edge(2, 3, weight=0.9)  # specify edge data

    G = nx.DiGraph()
    i=1
    myList = []
    myDict = {}
    while i < len(x):
        G.add_edge(i-1, i)
        i+=1
    G.add_edge(1,1)
    count = 0

    for entry in x:
        myList.append((int(x[count]), int(y[count])))
        count += 1
    lcv = 0
    for j in myList:
        myDict[lcv] = j
        lcv+=1

    print("My dictionary \n")
    print(myDict)
    options = {
        "font_size": 10,
        "node_size": 200,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 3,
        "width": 1,
    }
    nx.draw_networkx(G,myDict, **options)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    pass
"""
G = nx.Graph()
G.add_edge(1, 2)  # default edge data=1
G.add_edge(2, 3, weight=0.9)  # specify edge data
"""



"""
seed = 13648  # Seed random number generators for reproducibility
G = nx.random_k_out_graph(10, 3, 0.5, seed=seed)
pos = nx.spring_layout(G, seed=seed)

node_sizes = [3 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
cmap = plt.cm.plasma

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="indigo")
edges = nx.draw_networkx_edges(
    G,
    pos,
    node_size=node_sizes,
    arrowstyle="->",
    arrowsize=10,
    edge_color=edge_colors,
    edge_cmap=cmap,
    width=2,
)
# set alpha value for each edge
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

pc = mpl.collections.PatchCollection(edges, cmap=cmap)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()
plt.show()
"""


if __name__ == "__main__":
    randomDirectory()
    x, y, w = readDir()
    print(f"x = {x} y = {y} weight = {w}")
    connectDots(x, y, w)




