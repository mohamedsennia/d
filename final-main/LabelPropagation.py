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
            clusters,a=exe(G)
            
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
            clusters,a=exe(G)
            A+=a
            
        A=A/n
        As.append(A)
    if(show):
        dr.draw(sizes,As,"changement de nombre de choix aléatoire, par rapport au taille du graphe", "taille du graphe","nombre de choix aléatoire fait")
    return(sizes,As)


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
rateMod([G,G1,G],100,True)

