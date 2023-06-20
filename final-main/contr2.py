import networkx as nx
import draw as dr
import random
import numpy as np
import show as sh
import cr as crs
import modularité as modu
import urllib.request
import io
import zipfile
import datetime
def heh(G,H,T):
    nodes=list(G.nodes)
    nodes.sort()
    lengths=[]
    times=[]
    keys={}
    
    j=0
    for i in (nodes):
        keys[i]=j
        lengths.append(len(list(G.neighbors(i))))
        j+=1
    j=0
    lengths.sort()
    tresh=int((len(nodes)*H)/100)
    tresh=tresh-1
    inf=[]
    lengths.reverse()
    infNeighbors={}
    for i in (nodes):
        if(len(list(G.neighbors(i)))>=lengths[tresh]):
            inf.append(i)
            infNeighbors[i]=list(G.neighbors(i))
    
    m=len(list(G.nodes))
    i=1
    candidats={}
    for i in range(len(inf)): 
        candidats[inf[i]]=[]
        for j in range(len(inf)):
            if i!=j:
                L=[e for e in infNeighbors[inf[i]] if e in infNeighbors[inf[j]]]
                p=(len(L)*100)/m
                if(p>T):
                    candidats[inf[i]].append(inf[j])
    
    for key in candidats:
        if(len(candidats[key])>1):
            toRemove=[]
            for i in range(len(candidats[key])-1):
                for j in range(i,len(candidats[key])):
                    if(not(candidats[key][i] is candidats[candidats[key][j]])):
                        L1=[e for e in infNeighbors[key] if e in infNeighbors[candidats[key][i]]]
                        L2=[e for e in infNeighbors[key] if e in infNeighbors[candidats[key][j]]]
                        if(L1>L2):
                            toRemove.append(candidats[key][j])
                        else:
                            toRemove.append(candidats[key][i])
            toRemove=list(set(toRemove))
            for element in toRemove:
                candidats[key].remove(element)
                candidats[element].remove(key)
    
    clusters=np.zeros(len(nodes),dtype=int)
    
    cl=set()
    c=1
    for key in candidats:
        
        if(len(candidats[key])==0):
            clusters[keys[key]]=c
            if(c!=0):
                cl.add(key)
            c=c+1
        else:
            b=False
            for e in candidats[key]:
                if(clusters[keys[e]]!=0):
                    clusters[keys[key]]=clusters[keys[e]]
                    if(c!=0):
                        cl.add(key)
                    b=True
                    break
            if(b==False):
                clusters[keys[key]]=c
                if(c!=0):
                    cl.add(key)
                c=c+1
    clusters2={}
    
    for i in range(len(nodes)):
        clusters2[nodes[i]]=clusters[i]
    cl=list(clusters2.values())
    k=len(set(cl))
    clusters=[]
    for i in range(k):
        
        clusters.append([])
    pivot=[]
    for i in range(len(cl)):
        if(cl[i]!=0):
            pivot.append(i)
        clusters[cl[i]].append(i)
    print(clusters)
    AdjeMat=nx.to_numpy_array(G,dtype=int)
   
    clustersp=[]
    history=[]
    clus={}

    for i in range(len(clusters)):
        for c in clusters[i]:
            clus[c]=i+1
    
    while(clustersp!=clusters and clustersp not in history):
        if(clusters==clustersp):
            print(".")
        history.append(clustersp)
        clustersp=[]
        for c in clusters:
            clustersp.append(list(c[:]))
        mo=-1
        for n in nodes:
            if(n not in pivot):
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
    mat=modu.matAdj(G)
    m=modu.m(mat)
    print(clusters)

    print(modu.modularite(G,mat,clusters,m))
    
G1=nx.karate_club_graph()
heh(G1,10,50)