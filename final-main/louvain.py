import pandas as pd
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
import modularité as md
import show as sh
import draw as dr
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
    mods=[]
    sizes=[]
    for G in Gs:
        size=len(list(G.nodes))
        sizes.append(size)
        mods.append(exe(G,False))
    dr.draw(sizes,mods)
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G1=nx.from_edgelist(edgelist)  
G=nx.karate_club_graph()
rateMod([G,G1])