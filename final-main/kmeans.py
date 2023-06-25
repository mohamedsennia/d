import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import show as sh
import modularité as md
import draw as dr
import urllib.request
import io
import zipfile
import datetime
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
    clus={}

    for i in range(len(clusters)):
        for c in clusters[i]:
            clus[c]=i+1
    if(show==True):
        colors=sh.init_colors(clus)
    while(clustersp!=clusters and clustersp not in history):
        if(show==True):
            sh.show(G,list(clus.values()),colors)
        history.append(clustersp)
        clustersp=[]
        for c in clusters:
            clustersp.append(list(c[:]))
        mo=-1
        for n in nodes:
            mo=mo+1
            d=-1
            c=-1
            c0=-1
            
            for i in range(k):
                dt=0
                mel=-1
                for n2 in clusters[i]:
                    mel=mel+1
                    if(n2==n):
                        c0=i
                    if(AdjeMat[mo][mel]!=0):
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
        sh.show(G,list(clus.values()),colors)
    
    return list(clus.values())

            

def exe(G,k):
    sh.draw_first(G)
    clusters=Kmeans(G,k,True)
def evaluateK(G,kmax):
    mod=[]
    mat=md.matAdj(G)
    m=md.m(mat)
    ks=[]
    times=[]
    nodes=list(G.nodes())
    for i in range(2,kmax):
        start=datetime.datetime.now()
        clusters=Kmeans(G,i,False)
       
        end=datetime.datetime.now()
        diff=end-start
        times.append(diff.total_seconds())
        ks.append(i)
        clusters2={}
        for i in range(len(clusters)):
            if(clusters[i] in clusters2.keys()):
                clusters2[clusters[i]].append(nodes[i])
            else:
                clusters2[clusters[i]]=[nodes[i]]
            
        
        mod.append(nx.community.modularity(G,list(clusters2.values())))
    
    
    dr.draw(ks,mod,"changement de modularité en fonction de paramètre k","k","modularité")
    dr.draw(ks,times,"Temps d'exécution en fonction de k","k","Temps d'exécution (s)")
def evaluateN(Gs,k):
    mod=[]
    times=[]
    sizes=[]
    for G in Gs:
        nodes=list(G.nodes())
        mat=md.matAdj(G)
        m=md.m(mat)
        sizes.append(len(list(G.nodes())))
        start=datetime.datetime.now()
        clusters=Kmeans(G,k,False)
        
       
        end=datetime.datetime.now()
        clusters2={}
        for i in range(len(clusters)):
            if(clusters[i] in clusters2.keys()):
                
                clusters2[clusters[i]].append(nodes[i])
            else:
                clusters2[clusters[i]]=[nodes[i]]
        
        mod.append(nx.community.modularity(G,list(clusters2.values())))
        diff=end-start
        times.append(diff.total_seconds())
    
    dr.draw(sizes,mod,"changement de modularité en fonction de taille du graphe","Taille","modularité")
    dr.draw(sizes,times,"Temps d'exécution en fonction de la taille du graphe","Taille de graphe","Temps d'exécution (s)")
