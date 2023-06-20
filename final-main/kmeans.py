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
    print(AdjeMat)
    clustersp=[]
    history=[]
    clus={}

    for i in range(len(clusters)):
        for c in clusters[i]:
            clus[c]=i+1
    if(show==True):
        colors=sh.init_colors(clus)
    while(clustersp!=clusters and clustersp not in history):
        if(clusters==clustersp):
            print("aaaaaa")
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
    return clusters

            

def exe(G,k):
    sh.draw_first(G)
    clusters=Kmeans(G,k,True)
def evaluateK(G,kmax):
    mod=[]
    mat=md.matAdj(G)
    m=md.m(mat)
    ks=[]
    times=[]
    for i in range(2,kmax):
        start=datetime.datetime.now()
        clusters=Kmeans(G,i,False)
        end=datetime.datetime.now()
        diff=end-start
        times.append(diff.total_seconds())
        ks.append(i)
        mod.append(md.modularite(G,mat,clusters,m))
    dr.draw(ks,mod,"changement de modularité en fonction de paramètre k","k","modularité")
    dr.draw(ks,times,"Temps d'exécution en fonction de k","k","Temps d'exécution (s)")
def evaluateN(Gs,k):
    mod=[]
    times=[]
    sizes=[]
    for G in Gs:
        mat=md.matAdj(G)
        m=md.m(mat)
        sizes.append(len(list(G.nodes())))
        start=datetime.datetime.now()
        clusters=Kmeans(G,k,False)
        end=datetime.datetime.now()
        mod.append(md.modularite(G,mat,clusters,m))
        diff=end-start
        times.append(diff.total_seconds())
    print(sizes,mod)
    dr.draw(sizes,mod,"changement de modularité en fonction du taille de graphe","Taille","modularité")
    dr.draw(sizes,times,"Temps d'exécution en fonction de la taille de graphe","Taille de graphe","Temps d'exécution (s)")
G2=nx.karate_club_graph()
edgelist=[(0,1),(1,2),(2,3),(2,4),(2,5),(3,4),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9)]
G1=nx.from_edgelist(edgelist) 
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

evaluateK(G1,10)
evaluateN([G2,G1,G],2)