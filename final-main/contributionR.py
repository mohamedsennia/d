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
import pandas as pd
def exe(G,k,T,show):
  
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
    tresh=int((len(nodes)*k)/100)
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
    
    clusters,ran=crs.labelPropagation(G,nodes,clusters2,show)
    clusters=list(clusters.values())
    return clusters,ran

def rateMod(Gs,k,T,n,show):
    Mods=[]
    sizes=[]
    times=[]
    for G in Gs:
        
        nodes=list(G.nodes)
        nodes.sort()
        sizes.append(len(nodes))
        
        mod=0
        adj=modu.matAdj(G)
        m=modu.m(adj)
        
        for i in range(n):
            start=datetime.datetime.now()
            clusters2,ran=exe(G,k,T,False)
            
            end=datetime.datetime.now()
            adj=modu.matAdj(G)
            
            
            clusters={}
            for i in range(len(clusters2)):
                if(clusters2[i] in clusters.keys()):
                    clusters[clusters2[i]].append(nodes[i])
                else:
                    clusters[clusters2[i]]=[nodes[i]]
            
            mod+=nx.community.modularity(G,list(clusters.values()))
           
        mod=mod/n
        diff=end-start
        Mods.append(mod)
        times.append(diff.total_seconds())
    if(show):
        dr.draw(sizes,Mods,"changement de modularité par rapport au taille du graphe","taille du graphe","modularité")
        dr.draw(sizes,times,"Temps d'exécution en fonction de la taille du graphe","Taille du graphe","Temps d'exécution (s)")
    return(sizes,Mods,times)  
def rateModPerK(G,ks,T,n):
    Mods=[]
    Ks=[]
    times=[]
    for k in ks:
        nodes=list(G.nodes)
        nodes.sort()
        Ks.append(k)
        
        mod=0
        adj=modu.matAdj(G)
        m=modu.m(adj)
        for i in range(n):
            start=datetime.datetime.now()
            clusters2,ran=exe(G,k,T,False)
            end=datetime.datetime.now()
            clusters={}
            for i in range(len(clusters2)):
                if(clusters2[i] in clusters.keys()):
                    clusters[clusters2[i]].append(nodes[i])
                else:
                    clusters[clusters2[i]]=[nodes[i]]
            
            mod+=nx.community.modularity(G,list(clusters.values()))
            
        mod=mod/n
        diff=end-start
        times.append(float(diff.total_seconds()))
        Mods.append(mod) 
    print(Ks,Mods)      
    dr.draw(Ks,Mods,"changement de modularité par rapport au changement de k","k","modularité")
    dr.draw(Ks,times,"Temps d'exécution en fonction de k","k","Temps d'exécution (s)")
def rateModPerT(G,k,Ts,n):
    times=[]
    Mods=[]
    ts=[]
    for T in Ts:
        nodes=list(G.nodes)
        nodes.sort()
        ts.append(T)
        
        mod=0
        adj=modu.matAdj(G)
        m=modu.m(adj)
        for i in range(n):
            start=datetime.datetime.now()
            clusters2,ran=exe(G,k,T,False)
            end=datetime.datetime.now()
            clusters={}
            for i in range(len(clusters2)):
                if(clusters2[i] in clusters.keys()):
                    clusters[clusters2[i]].append(nodes[i])
                else:
                    clusters[clusters2[i]]=[nodes[i]]
            mod+=nx.community.modularity(G,list(clusters.values()))
            
        mod=mod/n
        diff=end-start
        times.append(float(diff.total_seconds()))
        Mods.append(mod) 
    print(ts,Mods)      
    dr.draw(ts,Mods,"changement de modularité par rapport au changement de T","T","modularité")
    dr.draw(ts,times,"Temps d'exécution en fonction de T","T","Temps d'exécution (s)")
def rateAs(Gs,k,T,n,show):
    As=[]
    sizes=[]
    for G in Gs:
        nodes=list(G.nodes)
        nodes.sort()
        sizes.append(len(nodes))
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T,False)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(sizes,As)  
    if(show):
        dr.draw(sizes,As,"changement de nombre de choix aléatoire par rapport au taille du graphe","taille du graphe","Choix aléatoire")
    return(sizes,As)
def rateAsPerK(G,ks,T,n):
    As=[]
    Ks=[]
    for k in ks:
        nodes=list(G.nodes)
        nodes.sort()
        Ks.append(k)
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T,False)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(Ks,As)  
    dr.draw(Ks,As,"changement de nombre de choix aléatoire par rapport au k","k","Choix aléatoire")
def rateAsPerT(G,k,Ts,n):
    As=[]
    ts=[]
    for T in Ts:
        nodes=list(G.nodes)
        nodes.sort()
        ts.append(T)
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T,False)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(ts,As)  
    dr.draw(ts,As,"changement de nombre de choix aléatoire par rapport au T","T","Choix aléatoire")




G1=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G2=nx.from_edgelist(edgelist)  
#rateMod([G1,G2],20,50,10)
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


exe(G1,20,70,True)


