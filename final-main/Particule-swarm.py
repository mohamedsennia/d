
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def modularte(G,X):
    N=set()
    Clusters=set(X)
    mod={}
    inOut={}
    for c in Clusters:
        inOut[c]={"in":0,
        "out":0
        }
        mod[c]=0
    for g in G:
        N.update(g)
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            if(X[i]==X[j]):
                if(j in G[i]):
                    inOut[X[i]]["in"]+=1
                else:
                    inOut[X[i]]["out"]+=1
    m=0
    for g in G:
        for g2 in g:
            m=m+1
    
    for j in inOut:
        mod[j]=(inOut[j]["in"]/m)-pow(((inOut[j]["out"]+inOut[j]["in"])/m),2)
    modularité=0
    for mo in mod:
        modularité+=mod[mo]
    return modularité
        
def sig(x):
    return 1/(1 + np.exp(-x))
def particule(G,R,Pbest,Gbest,X,V):
    x=X[:]
    omega=random.random()
    c1=1.494
    c2=1.494
    r1=random.random()
    r2=random.random()
    
    temp1=[]
    temp2=[]
    for i in range(len(X)):
        temp1.append(X[i]^Pbest[i])
        if(temp1[i]!=0):
            temp1[i]=1
        temp2.append(X[i]^Gbest[i])
        if(temp2[i]!=0):
            temp2[i]=1
        temp3=omega*V[i]+c1*r1*temp1[i]+c2*r2*temp2[i]
        randomNumber=random.random()
        if(randomNumber<sig(temp3)):
            V[i]=1
        else:
            V[i]=0
        C=set(X)
        
        Clusters={}
        for c in C:
            Clusters[c]=0
        if(V[i]==1):
            for k in range(len(G[i])):
                h=X[G[i][k]]
                Clusters[h]=Clusters[h]+1
            max=-1
            imax=-1
            for c in Clusters:
                
                if(Clusters[c]>max):
                    max=Clusters[c]
                    imax=c
            x[i]=imax
    if(modularte(G,x)>modularte(G,Pbest)):
        print("une meilleur position personelle a été trouver : ", x)
        print("old p mod:",modularte(G,Pbest))
        print("new p mod:",modularte(G,x))
        Pbest=x[:]
    if(modularte(G,x)>modularte(G,Gbest)):
        print("une meilleur position Global a été trouver : ", x)
        print("old G mod:",modularte(G,Gbest))
        print("new G mod:",modularte(G,x))
        Gbest=x[:]
    
    return x,V,Pbest,Gbest
G=[[1,2,3,5],[0,4,6],[0,3,5],[0,2],[1,6],[0,2],[1,4]]
R=[]
Pbest=[2,2,2,1,2,1,7]
Gbest=[1,1,1,1,2,2,2]

X=[1,2,2,4,2,2,7]
V=[0,0,0,0,0,0,0]
""""""
"""G = nx.karate_club_graph()
"""
edgelist= [(1,2),(1,3),(1,4),(1,6),(2,5),(2,7),(3,4),(3,6),(5,7)]
G=nx.from_edgelist(edgelist)
G=nx.karate_club_graph()
Mat=[]
nodes = list(G.nodes)
nodes.sort()
Pbest=[]
Gbest=[]
V=[]
X=[]
for i in range(1000):
    Pbest.append([])
    V.append([])
    X.append([])
    for n in nodes:
        Pbest[i].append(n)
        V[i].append(0)
        X[i].append(random.randint(min(nodes),max(nodes)))
for n in nodes: 
    Mat.append([(n-1) for n in G.neighbors(n)])
    Gbest.append(n)

nx.draw(G,with_labels=True,node_color='r')
plt.show() 

for i in range(20000):
        X[0],V[0],Pbest[0],Gbest=particule(Mat,R,Pbest[0],Gbest,X[0],V[0])

colors=[]
clusters=[i for i in set(Pbest[0])]

step=int(16777215/len(clusters))

for x in Pbest[0]:
    colors.append(str(hex(((clusters.index(x)+1)*step)-500)[2:]))
for i in range(len(colors)):
    for j in range(6-len(colors[i])):
        colors[i]="0"+colors[i]
    colors[i]="#"+colors[i]
temp=colors[4]
print(Gbest)
nx.draw(G,node_color=colors,with_labels=True)


plt.show() 
