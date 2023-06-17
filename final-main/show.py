import networkx as nx
import matplotlib.pyplot as plt
def show(G,clusters,clustersColors):
    colors=[]
    for c in clusters:
        colors.append(clustersColors[c-1])
    nx.draw_spring(G,node_color=colors)
    plt.show()
import networkx as nx
import matplotlib.pyplot as plt
def init_colors(clusters):
    colors=[]
    clustersset=[i for i in set(clusters)]
    
    step=int(16777215/len(clustersset))

    for x in clusters:
        colors.append(str(hex(((clustersset.index(x)+1)*step)-500)[2:]))
    for i in range(len(colors)):
        for j in range(6-len(colors[i])):
             colors[i]="0"+colors[i]
        colors[i]="#"+colors[i]
    return colors
def draw_first(G):
    nx.draw_spring(G,with_labels=True)
    plt.show()
