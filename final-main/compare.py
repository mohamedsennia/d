import LabelPropagation as LB
import contributionR as CR
import matplotlib.pyplot as plt
import numpy as np
import math
import urllib.request
import io
import zipfile
import networkx as nx

url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

sock = urllib.request.urlopen(url)  # open URL
s = io.BytesIO(sock.read())  # read into BytesIO "file"
sock.close()

zf = zipfile.ZipFile(s)  # zipfile object
txt = zf.read("football.txt").decode()  # read info file
gml = zf.read("football.gml").decode()  # read gml data
# throw away bogus first line with # from mejn files
gml = gml.split("\n")[1:]
G = nx.parse_gml(gml)  # parse gml data




options = {"node_color": "black", "node_size": 50, "linewidths": 0, "width": 0.1}

pos = nx.spring_layout(G, seed=1969)  # Seed for reproducible layout
G1=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G2=nx.from_edgelist(edgelist)   
# Using Numpy to create an array X

sizes,labelMod,times1=LB.rateMod([G2,G1,G],100,False)
sizes,contrMod,times2=CR.rateMod([G2,G1,G],50,50,100,False)
  
# Plotting both the curves simultaneously
plt.plot(sizes, times1, color='r', label='label propagation')
plt.plot(sizes, times2, color='g', label='contribution')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Taille du graphe")
plt.ylabel("Temps d'exécution")
plt.title("Comparaison du performance")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()
# Plotting both the curves simultaneously
plt.plot(sizes, labelMod, color='r', label='label propagation')
plt.plot(sizes, contrMod, color='g', label='contribution')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Taille du graphe")
plt.ylabel("Modularité")
plt.title("Comparaison du performance")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()




sizes,labelA=LB.rateA([G2,G1,G],100,False)
sizes,contrA=CR.rateAs([G2,G1,G],50,50,100,False)
# Plotting both the curves simultaneously
plt.plot(sizes, labelA, color='r', label='label propagation')
plt.plot(sizes, contrA, color='g', label='contribution')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Taille du graphe")
plt.ylabel("Modularité")
plt.title("Comparaison du performance")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()