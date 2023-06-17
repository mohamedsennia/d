import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def labelPropagation(G,nodes,clusters,show):
    aléatoire=0
    while(0 in clusters):
        i=random.randint(0,len(clusters)-1)
        
        if(clusters[i]==0):
            adj=np.zeros(len(set(clusters)),dtype=int)
            for n in(list(G.neighbors(nodes[i]))):
                if(clusters[n]!=0):
                    adj[clusters[n]-1]=adj[clusters[n]-1]+1
            clusters[i]=(np.argmax(adj)+1)
            joe=np.where(adj == np.amax(adj))[0]
            if(joe.size>1):
                aléatoire+=1
            mama=random.randint(0,joe.size-1)
            clusters[i]=(joe[mama])+1
           
            
    return clusters,aléatoire
