from tqdm import tqdm
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.animation import FuncAnimation
import tsplib95
import networkx as nx
import pickle
import time

# getting data from tsplib95 data
problem = tsplib95.load_problem('Vrp-All/A/A-n32-k5.vrp')
fig, ax = plt.subplots()
G = problem.get_graph()
edge_list = list(problem.get_edges())
e = []
# to keep the position of the nodes in the plot fixed
pos = problem.node_coords

def update(num):
    ax.clear()
    e.append(edge_list[num+1])
    nx.draw(G, pos=pos, with_labels = True, edgelist=e, edge_color='red')
    ax.set_title("Frame %d:    "%(num+1), fontweight="bold")

ani = FuncAnimation(fig, update, frames=len(edge_list))
plt.show()
