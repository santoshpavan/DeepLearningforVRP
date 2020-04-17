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
import io

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
    #ax.clear()
    if num<=len(node_list):
        node_color_values[num] = (1,0,0)
    im_io = io.BytesIO()
    #edge color is white to ignore it
    nx.draw(G, pos=pos, with_labels=False, node_color=node_color_values, node_size=20, edge_color=(1,1,1))
    fig.savefig(im_io,dpi=5) #this makes the image=(64,47)
    im = Image.open(im_io)
    
ani = FuncAnimation(fig, update, frames=len(edge_list))
plt.show()
"""
import io
im_io = io.BytesIO()
#nx.draw(G)
nx.draw(G, pos=pos, with_labels = False, node_color=(1,0,0), node_size=20, edge_color=(1,1,1))
fig.savefig(im_io,dpi=5) #this makes the image=(32,24)
im = Image.open(im_io) #results in ImagePNGPlugin object not Image
#a = im.split()
#print(a)
l = im.getdata()
print(l)
d = [[i[0],i[1],i[2]] for i in l]
n = np.array(d)
im = Image.fromarray(n)
print(type(im))
#im = im.resize((1000,1000))
#im.show() # will show the image directly
#plt.show() # will show the graph through matplotlib
cv2.imshow("image",np.array(im))
#im.close()
#print(im.size)
#"""
