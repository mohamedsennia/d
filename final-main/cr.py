import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import show as sh
import urllib.request
import io
import zipfile
def labelPropagation(G,nodes,clusters,show):
    clustersv=clusters.values()
    colors=sh.init_colors(clustersv)
    if(show):
            sh.show(G,clustersv,colors)
    aléatoire=0
    while(0 in clustersv):
        
        i=random.randint(0,len(clusters)-1)
        
        if(clusters[nodes[i]]==0):
            if(show):
                sh.show(G,clustersv,colors)
            adj=np.zeros(len(set(clusters)),dtype=int)
            for n in(list(G.neighbors(nodes[i]))):
                if(clusters[n]!=0):
                    adj[clusters[n]-1]=adj[clusters[n]-1]+1
            clusters[nodes[i]]=(np.argmax(adj)+1)
            joe=np.where(adj == np.amax(adj))[0]
            if(joe.size>1):
                aléatoire+=1
            mama=random.randint(0,joe.size-1)
            clusters[nodes[i]]=(joe[mama])+1
    if(show):
        sh.show(G,clustersv,colors)
    return clusters,aléatoire
