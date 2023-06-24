import contributionR as CR
import girvan 
import kmeans as km
import louvain
import LabelPropagation as LB
import networkx as nx
import urllib.request
import io
import zipfile

import pandas as pd
def execute(G,params,algo):
    if(algo==1):
        LB.exe(G,True)
    elif(algo==2):
        CR.exe(G,params["k"],params["T"],True)
    elif(algo==3):
        km.Kmeans(G,params["k"],True)
    elif(algo==4):
        girvan.new_grivan(G,params["k"],True)
    elif(algo==5):
        louvain.exe(G,True)
def testModPerK(G,algo):
    if(algo==3):
        km.evaluateK(G,10)
    if(algo==4):
        girvan.ratePerK(G,10)
    if(algo==2):
        CR.rateModPerK(G,[10,20,30,40,50,60,70,80,90],50,100)
def testModPerT(G):
    CR.rateModPerT(G,10,[10,20,30,40,50,60,70,80,90],100)
def testModN(G,algo):
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
    if(algo==1):
        LB.rateMod([G1,G2,G],100,False)
    elif(algo==2):
        CR.rateMod([G1,G2,G],50,50,100,False)
    elif(algo==3):
        km.Kmeans([G1,G2,G],2)
    elif(algo==4):
        girvan.ratePerGraph([G1,G2,G],2)
    elif(algo==5):
        louvain.rateMod([G1,G2,G])
def rateA(G,algo,param):
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
    
    if(algo==1):
        LB.rateA([G1,G2,G],100,False)
    else:
        if(param=="k"):
            CR.rateAsPerK(G1,[10,20,30,40,50,60,70,80,90],50,100)
        elif(param=="T"):
            CR.rateAsPerT(G1,10,[10,20,30,40,50,60,70,80,90],100)
        else:
            CR.rateAs([G1,G2,G,100],10,50,100,False)