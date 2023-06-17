import networkx as nx
import matplotlib.pyplot as plt
import modularité as mod
import draw as dr
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
    matAdj=mod.matAdj(G)
    m=mod.m(matAdj)
    for k in range(2,Kmax):
        Ks.append(k)
        clusters=new_grivan(G,k,False)
        modularites.append(mod.modularite(G,matAdj,clusters,m))
    dr.draw(Ks,modularites)
def ratePerGraph(Gs,k):
    modularites=[]
    sizes=[]
    
    for G in Gs:
        matAdj=mod.matAdj(G)
        m=mod.m(matAdj)
        sizes.append(len(list(G.nodes())))
        clusters=new_grivan(G,k,False)
        modularites.append(mod.modularite(G,matAdj,clusters,m))
    print(sizes,modularites)
    dr.draw(sizes,modularites)
    
G=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G2=nx.from_edgelist(edgelist)
ratePerGraph([G,G2],3)