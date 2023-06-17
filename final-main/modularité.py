
def m(Mat):
    m=0
    for g in Mat:
        for g2 in g:
            m=m+1
    return m
def modularite(G,mat,clusters,m):
    modularite=0
    nodes=list(G.nodes())
    
    for i in range(len(clusters)):
        for j in  range(i,len(clusters)):
            if(clusters[i]==clusters[j]):
                if(j+1 in mat[i]):
                    
                    modularite+=1-((len(list(G.neighbors(nodes[i])))*len(list(G.neighbors(nodes[j]))))/m)
                else:
                    modularite+=0-((len(list(G.neighbors(nodes[i])))*len(list(G.neighbors(nodes[j]))))/m)
    modularite=modularite/m
    return modularite
def matAdj(G):
    nodes = list(G.nodes)
    Mat=[]
    for n in nodes: 
        Mat.append([n for n in range(len(list(G.neighbors(n))))])
    
    return Mat