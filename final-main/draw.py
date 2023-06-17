import matplotlib.pyplot as plt
def draw(x,y,title,xname,yname):
    # Creating figure
    fig = plt.figure()
    
    # Adding axes on the figure
    ax = fig.add_subplot(111)
    ax.set_title(title, fontsize=15)
 
    # Adding axis title
    ax.set_xlabel(xname, fontsize=12)
    ax.set_ylabel(yname, fontsize=12)
    plt.plot(x,y)
    plt.show()