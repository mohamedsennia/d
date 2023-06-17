import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
def labelPropagation(G,nodes,clusters):
    ns=nodes
    
    while(0 in clusters):
        print(clusters)
        for j in range(1):
            i=random.randint(0,len(ns)-1)
            print(ns[i])
            if(clusters[ns[i]]==0):
                adj=np.zeros(len(set(clusters)),dtype=int)
                for n in(list(G.neighbors(ns[i]))):
                    if(clusters[n]!=0):
                        adj[clusters[n]-1]=adj[clusters[n]-1]+1
                clusters[i]=(np.argmax(adj)+1)
                ns.pop(i)
    return clusters
                    

G=nx.karate_club_graph()
inf=[]
infNeighbors={}
nodes=list(G.nodes)
nodes.sort()
for i in (nodes):
    if(len(list(G.neighbors(i)))>9):
        inf.append(i)
        infNeighbors[i]=list(G.neighbors(i))
#
m=len(list(G.nodes))
i=1
candidats={}

for i in range(len(inf)): 
    candidats[inf[i]]=[]
    for j in range(len(inf)):
        if i!=j:
            L=[e for e in infNeighbors[inf[i]] if e in infNeighbors[inf[j]]]
            p=(len(L)*100)/m
            if(p>15):
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
c=1
for key in candidats:
    
    if(len(candidats[key])==0):
        clusters[key]=c
        c=c+1
    else:
        b=False
        for e in candidats[key]:
            if(clusters[e]!=0):
                clusters[key]=clusters[e]
                b=True
                break
        if(b==False):
            clusters[key]=c
            c=c+1

clusters=labelPropagation(G,nodes,clusters)

colors=[]
for cluster in clusters:
    if(cluster==1):
        colors.append("#FF0000")
    if(cluster==2):
        colors.append("#00FF00")
    if(cluster==3):
        colors.append("#0000FF")
nx.draw(G,node_color=colors,with_labels=True)


plt.show() 
