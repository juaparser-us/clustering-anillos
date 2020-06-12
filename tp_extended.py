import numpy as np
import matplotlib.pyplot as plt
import math
from schema import Cluster

def get_circle(clusters, points):

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    fig, ax = plt.subplots()

    ax.set(xlim=(0, 30), ylim = (0, 25))

    for c in clusters:
        xc = c.center[0];
        yc = c.center[1];
        ax.scatter(xc,yc, marker="x", c=c.color)
        if(len(c.belonging)!=0):
            m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in c.belonging];
            r = np.mean(m);
        else:
            r = c.radius
        a_circle = plt.Circle((c.center[0], c.center[1]), r,fill=False,color=c.color)
        ax.add_artist(a_circle)
        for p in c.belonging:
            ax.scatter(p[0],p[1], c=c.color)
    
  
    plt.show();

