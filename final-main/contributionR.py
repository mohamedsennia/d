import networkx as nx
import draw as dr
import random
import numpy as np
import show as sh
import cr as crs
import modularité as modu
def exe(G,k,T):
  
    nodes=list(G.nodes)
    nodes.sort()
    lengths=[]
    for i in (nodes):
        lengths.append(len(list(G.neighbors(i))))
        
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
            clusters[key]=c
            if(c!=0):
                cl.add(key)
            c=c+1
        else:
            b=False
            for e in candidats[key]:
                if(clusters[e]!=0):
                    clusters[key]=clusters[e]
                    if(c!=0):
                        cl.add(key)
                    b=True
                    break
            if(b==False):
                clusters[key]=c
                if(c!=0):
                    cl.add(key)
                c=c+1
    clusters,ran=crs.labelPropagation(G,nodes,clusters,True)
    print(clusters)
    return clusters,ran

def rateMod(Gs,k,T,n):
    Mods=[]
    sizes=[]
    for G in Gs:
        nodes=list(G.nodes)
        nodes.sort()
        sizes.append(len(nodes))
        
        mod=0
        adj=modu.matAdj(G)
        m=modu.m(adj)
        for i in range(n):
            
            clusters2,ran=exe(G,k,T)
            adj=modu.matAdj(G)
            mod+=modu.modularite(G,adj,clusters2,m)
        mod=mod/n
        Mods.append(mod) 
    print(sizes,Mods)      
    dr.draw(sizes,Mods)
def rateModPerK(G,ks,T,n):
    Mods=[]
    Ks=[]
    for k in ks:
        nodes=list(G.nodes)
        nodes.sort()
        Ks.append(k)
        
        mod=0
        adj=modu.matAdj(G)
        m=modu.m(adj)
        for i in range(n):
            
            clusters2,ran=exe(G,k,T)
            adj=modu.matAdj(G)
            mod+=modu.modularite(G,adj,clusters2,m)
        mod=mod/n
        Mods.append(mod) 
    print(Ks,Mods)      
    dr.draw(Ks,Mods)
def rateModPerT(G,k,Ts,n):
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
            
            clusters2,ran=exe(G,k,T)
            adj=modu.matAdj(G)
            mod+=modu.modularite(G,adj,clusters2,m)
        mod=mod/n
        Mods.append(mod) 
    print(ts,Mods)      
    dr.draw(ts,Mods)
def rateAs(Gs,k,T,n):
    As=[]
    sizes=[]
    for G in Gs:
        nodes=list(G.nodes)
        nodes.sort()
        sizes.append(len(nodes))
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(sizes,As)  
    dr.draw(sizes,As)
def rateAsPerK(G,ks,T,n):
    As=[]
    Ks=[]
    for k in ks:
        nodes=list(G.nodes)
        nodes.sort()
        Ks.append(k)
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(Ks,As)  
    dr.draw(Ks,As)
def rateAsPerK(G,k,Ts,n):
    As=[]
    ts=[]
    for T in Ts:
        nodes=list(G.nodes)
        nodes.sort()
        ts.append(T)
        
        H=0
        for i in range(n):
            
            clusters2,ran=exe(G,k,T)
            H=H+ran
            print(ran)
        H=H/n
        print(H)
        As.append(H)
    print(ts,As)  
    dr.draw(ts,As)
G1=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G2=nx.from_edgelist(edgelist)  
rateMod([G1,G2],20,50,10)




