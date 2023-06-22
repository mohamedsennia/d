import pandas as pd
data = pd.read_csv("musae_facebook_edges.csv")
edgelist=[]

for i in range(len(data.loc[:])):
    edgelist.append((data.loc[i]["id_1"],data.loc[i]["id_2"]))
print(edgelist)