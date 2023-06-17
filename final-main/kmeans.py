import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import show as sh
import modularité as md
import draw as dr
def Kmeans(G,k,show):
    nodes=list(G.nodes)
    clusters=[]
    for i in range(k):
        clusters.append([])
    for n in nodes:
        rin=random.randint(0,k-1)
        clusters[rin].append(n)
    AdjeMat=nx.to_numpy_array(G,dtype=int)
    clustersp=[]
    history=[]
    clus=np.zeros(len(nodes),dtype=int)
    for i in range(len(clusters)):
        for c in clusters[i]:
            clus[c]=i+1
    if(show==True):
        colors=sh.init_colors(clus)
    while(clustersp!=clusters and clustersp not in history):
        history.append(clustersp)
        clustersp=[]
        for c in clusters:
            clustersp.append(list(c[:]))
            
        for n in nodes:
            d=-1
            c=-1
            c0=-1
            
            for i in range(k):
                dt=0
                for n2 in clusters[i]:
                    if(n2==n):
                        c0=i
                    if(AdjeMat[n][n2]!=0):
                        dt=dt+1
                if(len(clusters[i])!=0):
                    dt=dt/len(clusters[i])
                else:
                    dt=dt/1
                if(dt>d):
                    d=dt
                    c=i
            clusters[c0].remove(n)
            clusters[c].append(n)
            
        for i in range(len(clustersp)):
            for c in clustersp[i]:
                clus[c]=i+1
    if(show==True):
        sh.show(G,clus,colors)
    return clusters

            

def exe(G,k):
    sh.draw_first(G)
    clusters=Kmeans(G,k,True)
def evaluateK(G,kmax):
    mod=[]
    mat=md.matAdj(G)
    m=md.m(mat)
    ks=[]
    for i in range(2,kmax):
        clusters=Kmeans(G,i,False)
        ks.append(i)
        mod.append(md.modularite(G,mat,clusters,m))
    dr.draw(ks,mod)
def evaluateN(Gs,k):
    mod=[]
    sizes=[]
    for G in Gs:
        mat=md.matAdj(G)
        m=md.m(mat)
        sizes.append(len(list(G.nodes())))
        clusters=Kmeans(G,k,False)
        mod.append(md.modularite(G,mat,clusters,m))
    print(sizes,mod)
    dr.draw(sizes,mod)

G=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G1=nx.from_edgelist(edgelist) 
evaluateN([G1,G],4)