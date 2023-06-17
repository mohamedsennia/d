import networkx as nx
import matplotlib.pyplot as plt
import random
import show as sh
import modularité as md
import numpy as np
import draw as dr
def labelPropagation(G,nodes,clusters,show):
    a=0
    ns=nodes
    for n in ns:
        clu={}
        neighbors=G.neighbors(n)
        for neighbor in neighbors:
            if(clusters[neighbor] in clu):
                clu[clusters[neighbor]]+=1
            else:
                clu[clusters[neighbor]]=1
        max_keys = [key for key, value in clu.items() if value == max(clu.values())]
        if(len(max_keys)>1):
            a+=1
        clusters[n]=max_keys[0]
    return clusters,a
def exe(G):
    noeuds=[]
    noeuds=list(G.nodes)
    clusters=[]
    for i in range(len(noeuds)):
        clusters.append(i+1)
    sh.draw_first(G)    
    clusters=labelPropagation(G,noeuds,clusters,True)
    print(clusters)
def rateMod(Gs,n):
    mods=[]
    sizes=[]
    for G in Gs:
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        clusters=[]
        for i in range(len(noeuds)):
            clusters.append(i+1)
        mod=0
        mat=md.matAdj(G)
        m=md.m(mat)
        for i in range(n):
            clusters,a=labelPropagation(G,noeuds,clusters,False)
            mod+=md.modularite(G,mat,clusters,m)
            clusters=[]
            noeuds=list(G.nodes)
            for i in range(len(noeuds)):
                clusters.append(i+1)
        mod=mod/n
        mods.append(mod)
    print(sizes,mods)
    dr.draw(sizes,mods)
def rateA(Gs,n):
    As=[]
    sizes=[]
    for G in Gs:
        A=0
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        clusters=[]
        for i in range(len(noeuds)):
            clusters.append(i+1)
        for i in range(n):
            clusters,a=labelPropagation(G,noeuds,clusters,False)
            A+=a
            clusters=[]
            noeuds=list(G.nodes)
            for i in range(len(noeuds)):
                clusters.append(i+1)
        A=A/n
        As.append(A)
    print(sizes,As)
    dr.draw(sizes,As)
  
import urllib.request
import io
import zipfile

import matplotlib.pyplot as plt
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

print(txt)
# print degree for each team - number of games
for n, d in G.degree():
    print(f"{n:20} {d:2}")

options = {"node_color": "black", "node_size": 50, "linewidths": 0, "width": 0.1}

pos = nx.spring_layout(G, seed=1969)  # Seed for reproducible layout
nx.draw(G, pos, **options)
plt.show()
