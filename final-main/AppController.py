import Label_Propagation as LB
import contributionR as CR
import kmeans as km
import particuleSwarm as sm
def execute(G,params,algo):
    if(algo==1):
        LB.exe(G)
    elif(algo==2):
        CR.exe(G,params)
    elif(algo==3):
        km.Kmeans(G,params)