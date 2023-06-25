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
import datetime
import pandas as pd
def labelPropagation(G,nodes,clusters,show):
    a=0
    ns=nodes
    if(show==True):
        colors=sh.init_colors(clusters)
        sh.show(G,clusters,colors)
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
        if(show==True):
            sh.show(G,list(clusters.values()),colors)
    print(clusters)
    return clusters,a
def exe(G,show):
    noeuds=[]
    noeuds=list(G.nodes)
    clusters={}
    for i in range(len(noeuds)):
        clusters[noeuds[i]]=i+1

    
    clusters,ran=labelPropagation(G,noeuds,clusters,True)
    return clusters,ran
    
def rateMod(Gs,n,show):
    mods=[]
    sizes=[]
    times=[]
    for G in Gs:
        start=datetime.datetime.now()
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        
        
        
        
        mod=0
        mat=md.matAdj(G)
        m=md.m(mat)
        for i in range(n):
            start=datetime.datetime.now()
            clusters,a=exe(G,False)
            
            clusters=list(clusters.values())
            clusters2={}
            for i in range(len(clusters)):
                if(clusters[i] in clusters2.keys()):
                    clusters2[clusters[i]].append(noeuds[i])
                else:
                    clusters2[clusters[i]]=[noeuds[i]]

            now=datetime.datetime.now()
            
            ma=nx.community.modularity(G,list(clusters2.values()))
            mod+=ma
            
        mod=mod/n
        mods.append(mod)
       
        diff=now-start
        times.append(diff.total_seconds())
    if(show):
        dr.draw(sizes,mods,"changement du modulairté par rapport au taille du graphe","taille du graphe","modularité")
        dr.draw(sizes,times,"Temps d'exécution en fonction de taille du graphe","taille du graphe","Temps d'exécution (s)")
    return(sizes,mods,times)
def rateA(Gs,n,show):
    As=[]
    sizes=[]
    for G in Gs:
        A=0
        noeuds=[]
        noeuds=list(G.nodes)
        sizes.append(len(noeuds))
        
        for i in range(n):
            clusters,a=exe(G,False)
            A+=a
            
        A=A/n
        As.append(A)
    if(show):
        dr.draw(sizes,As,"changement de nombre de choix aléatoire, par rapport au taille du graphe", "taille du graphe","nombre de choix aléatoire fait")
    return(sizes,As)


