import networkx as nx
import matplotlib.pyplot as plt
import random
import show as sh
import modularité as md
import numpy as np
import draw as dr
import urllib.request
import io
import zipfile

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
    clusters={}
    for i in range(len(noeuds)):
        clusters[noeuds[i]]=i+1

    colors=sh.init_colors(list(clusters.values()))    
    clusters,ran=labelPropagation(G,noeuds,clusters,True)
    return clusters,ran
    
def rateMod(Gs,n):
    mods=[]
    sizes=[]
    for G in Gs:
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        
        mod=0
        mat=md.matAdj(G)
        m=md.m(mat)
        for i in range(n):
            clusters,a=exe(G)
            ma=md.modularite(G,mat,list(clusters.values()),m)
            mod+=ma
            
        mod=mod/n
        mods.append(mod)
    print(sizes,mods)
    dr.draw(sizes,mods,"changement de modulairté par rapport au taille de graphe","taille de graphe","modularité")
def rateA(Gs,n):
    As=[]
    sizes=[]
    for G in Gs:
        A=0
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        
        for i in range(n):
            clusters,a=exe(G)
            A+=a
            
        A=A/n
        As.append(A)
    print(sizes,As)
    dr.draw(sizes,As,"changement de nombre de choix aléatoire, par rapport au taille de graphe", "taille de graphe","nombre de choix aléatoire fait")
  


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
rateA([G,G1,G2],100)