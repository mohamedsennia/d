import networkx as nx
import matplotlib.pyplot as plt
import modularité as mod
import draw as dr
import urllib.request
import io
import zipfile
import datetime
def new_grivan(G,k,show):
    G2=G
    a=nx.connected_components(G)
    number_of_clusters=len(list(a))
    while(number_of_clusters<k):
        a=nx.connected_components(G)
        number_of_clusters=len(list(a))
        edge_betweenness=nx.edge_betweenness_centrality(G).items()
        edge_to_delete=sorted(edge_betweenness,key=lambda pair:-pair[1])[0][0]
        G.remove_edge(*edge_to_delete)
        if(show==True):
            nx.draw_spring(G)
            plt.show()
        a=nx.connected_components(G)
    
        a=nx.connected_components(G)
        number_of_clusters=len(list(a))
    a=nx.connected_components(G)
    comp=list(a)
    nodes=list(G.nodes())
    clusters=[]
    for n in (nodes):
        num=1
        for com in comp:
            if(n in com):
                clusters.append(num)
            num=num+1
    
    return clusters
            
def ratePerK(G,Kmax):
    modularites=[]
    Ks=[]
    times=[]
    matAdj=mod.matAdj(G)
    m=mod.m(matAdj)
    noeuds=list(G.nodes())
    for k in range(2,Kmax):
        start=datetime.datetime.now()
        Ks.append(k)
        clusters=new_grivan(G,k,False)
        end=datetime.datetime.now()
        diff=end-start
        times.append(diff.total_seconds())
        
        clusters2={}
        for i in range(len(clusters)):
            if(clusters[i] in clusters2.keys()):
                clusters2[clusters[i]].append(noeuds[i])
            else:
                clusters2[clusters[i]]=[noeuds[i]]
        modularites.append(nx.community.modularity(G,list(clusters2.values())))
        
    dr.draw(Ks,modularites,"changement de modularité par rapport au changement de k","valeurs de k","modularité")
    dr.draw(Ks,times,"Temps d'exécution en fonction de k","k","Temps d'exécution (s)")
def ratePerGraph(Gs,k):
    modularites=[]
    sizes=[]
    times=[]

    for G in Gs:
        noeuds=list(G.nodes())
        start=datetime.datetime.now()
        matAdj=mod.matAdj(G)
        m=mod.m(matAdj)
        sizes.append(len(list(G.nodes())))
        clusters=new_grivan(G,k,False)
        end=datetime.datetime.now()
        diff=end-start
        times.append(diff.total_seconds())
        clusters2={}
        for i in range(len(clusters)):
            if(clusters[i] in clusters2.keys()):
                clusters2[clusters[i]].append(noeuds[i])
            else:
                clusters2[clusters[i]]=[noeuds[i]]
        modularites.append(nx.community.modularity(G,list(clusters2.values())))
    print(sizes,modularites)
    dr.draw(sizes,modularites,"changement de modularité par rapport au changement de taille du graphe","taille du graphe","modularité")
    dr.draw(sizes,times,"Temps d'exécution en fonction de taille du graphe","Taille du graphe","Temps d'exécution (s)")
    
