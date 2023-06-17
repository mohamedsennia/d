import networkx as nx
import matplotlib.pyplot as plt
edgelist=[(1,2),(2,3),(3,4),(3,5),(3,6),(4,5),(6,7),(6,8),(7,8),(8,9),(8,10),(9,10)]
G=nx.from_edgelist(edgelist)
colors=[]
for i in range(10):
    colors.append("green")
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[2],colors[7]="red","blue"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[1]="red"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[6]="blue"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[8]="blue"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[5]="blue"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[9]="blue"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[3]="red"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[4]="red"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()
colors[0]="red"
nx.draw(G,node_color=colors,with_labels = True)
plt.show()