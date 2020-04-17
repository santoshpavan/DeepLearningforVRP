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
#node_color_values = [(0,0,1) for i in range(len(node_list))]
# to keep the position of the nodes in the plot fixed
pos = problem.node_coords
# the image size is (640, 480)
env = np.zeros((100,100,3), dtype=np.uint8)
color = (255,255,255)
path = [1,5,6,8]
for i in pos.keys():
    coods = pos.get(i)
    env[int(coods[0])][int(coods[1])] =  color
for visited_node in path:
    coods = pos.get(visited_node)
    env[int(coods[0])][int(coods[1])] = (255,0,0)
img = Image.fromarray(env,'RGB')
#print(env)
#print(type(img))
img = img.resize((300,300))
print(img.size)
#img.show()
#print(str(w)+" "+str(h))
#cv2.namedWindow('image', WINDOW_NORMAL)
#cv2.resizeWindow('image', 100,100)
cv2.imshow("image", np.array(img))
#cv2.waitKey(1)
