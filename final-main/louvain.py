import pandas as pd
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
import modularité as md
import show as sh
import draw as dr
import urllib.request
import io
import zipfile
import datetime
def exe(G,show):
    nodes=list(G.nodes())
    clusters={}
    clustersRep={}
    for i in range(len(nodes)):
        clusters[nodes[i]]=i+1

    clustersRep=clusters.copy()


    adj=md.matAdj(G)
    m=md.m(adj)
    mod=md.modularite(G,adj,list(clusters.values()),m)
    b=False
    colors=sh.init_colors((list(clusters.values())))
    while(b==False):
        b=True
        for i in range(len(nodes)):
            for n in G.neighbors(nodes[i]):
                if(clustersRep[nodes[i]]!=clustersRep[n]):
                    clustersRep[nodes[i]]=clustersRep[n]
                    modTemp=md.modularite(G,adj,list(clustersRep.values()),m)
                    if(modTemp>mod):
                        b=False
                        mod=modTemp
                        clusters=clustersRep.copy()
                        if(show==True):
                            sh.show(G,list(clusters.values()),colors)
                    else:
                        clustersRep=clusters.copy()
    if(show==True):
        sh.show(G,list(clusters.values()),colors)
    return(mod)
def rateMod(Gs):
    times=[]
    mods=[]
    sizes=[]
    for G in Gs:
        size=len(list(G.nodes))
        sizes.append(size)
        start=datetime.datetime.now()
        mods.append(exe(G,False))
        end=datetime.datetime.now()
        diff=end-start
        times.append(diff.total_seconds())
    dr.draw(sizes,mods,"changement de modularité par rapport au taille du graphe","taille du graphe","modularité")
    dr.draw(sizes,times,"Temps d'exécution en fonction de la taille du graphe","Taille du graphe","Temps d'exécution (s)")
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G1=nx.from_edgelist(edgelist)  
G2=nx.karate_club_graph()
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
rateMod([G,G2,G1])