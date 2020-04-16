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
node_list = list(problem.get_nodes())
node_color_values = [(0,0,1) for i in range(len(node_list))]
# to keep the position of the nodes in the plot fixed
pos = problem.node_coords
"""
def update(num):
    ax.clear()
    if num<=len(node_list):
        node_color_values[num] = (1,0,0)
    #edge color is white to ignore it
    nx.draw(G, pos=pos, with_labels = False, node_color=node_color_values, node_size=20, edge_color=(1,1,1))

ani = FuncAnimation(fig, update, frames=len(edge_list))
plt.show()
"""
import io
im_io = io.BytesIO()
#nx.draw(G)
nx.draw(G, pos=pos, with_labels = False, node_color=(1,0,0), node_size=10, edge_color=(1,1,1))
fig.savefig(im_io, format='png',dpi=10)
im = Image.open(im_io)
#im = im.resize((10,10))
im.show()
print(im.size)
