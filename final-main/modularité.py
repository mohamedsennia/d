"""def modularte(G,Mat,X):
    
    N=set()
   
    Clusters=set(X)
    mod={}
    inOut={}
    for c in Clusters:
        inOut[c]={"in":0,
        "out":0
        }
        mod[c]=0
    for g in Mat:
        N.update(g)
    
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            if(X[i]==X[j]):
                
                if(j in Mat[i]):
                    inOut[X[i]]["in"]+=1
                else:
                    inOut[X[i]]["out"]+=1
                 
    m=0
   
    for g in Mat:
        for g2 in g:
            m=m+1
    print(m)
    N=list(G.nodes)
    for i in range(len(N)):
        for j in range(i,len(N)):
            


    return modularité"""
def m(Mat):
    m=0
    for g in Mat:
        for g2 in g:
            m=m+1
    return m
def modularite(G,mat,clusters,m):
    modularite=0
    for i in range(len(clusters)):
        for j in  range(i,len(clusters)):
            if(clusters[i]==clusters[j]):
                if(j+1 in mat[i]):
                    modularite+=1-((len(list(G.neighbors(i)))*len(list(G.neighbors(j))))/m)
                else:
                    modularite+=0-((len(list(G.neighbors(i)))*len(list(G.neighbors(j))))/m)
    modularite=modularite/m
    """modularite=0
    
    for c in clusters:
        for i in range(len(c)):
            for j in range(i,len(c)):
                if(c[j] in mat[i]):
                    modularite+=1-((len(list(G.neighbors(c[i])))*len(list(G.neighbors(c[i]))))/m)
                else:
                    modularite+=0-((len(list(G.neighbors(c[i])))*len(list(G.neighbors(c[i]))))/m)"""
    return modularite
def matAdj(G):
    nodes = list(G.nodes)
    Mat=[]
    for n in nodes: 
        Mat.append([(n-1) for n in G.neighbors(n)])
    
    return Mat