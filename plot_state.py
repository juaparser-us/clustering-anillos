import numpy as np
import matplotlib.pyplot as plt
import math
from schema import Cluster

def initial_plot(clusters,points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    __, ax = plt.subplots()

    ax.set(xlim=(0, 25), ylim = (0, 30))

    for c in clusters:
        xc = c.center[0]
        yc = c.center[1]
        ax.scatter(xc,yc, marker="x", c=c.color)
        if(len(c.belonging)!=0):
            m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in c.belonging]
            r = np.mean(m)
        else:
            r = c.radius
        a_circle = plt.Circle((c.center[0], c.center[1]), r,fill=False,color=c.color)
        ax.add_artist(a_circle)
        for p in points:
            ax.scatter(p[0],p[1],color='#000000')

    plt.show()

def plot_state(clusters, points):

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    fig, ax = plt.subplots()

    ax.set(xlim=(0, 30), ylim = (0, 25))

    for c in clusters:
        belongings = c.belonging.keys()
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
        for p in belongings:
            ax.scatter(p[0],p[1], c=c.color)
    
  
    plt.show();

"""
points = [(9, 8), (7, 7.3), (6, 5), (12, 5), (9, 2), (11, 2.7), (6.4, 3.5), (11, 7.2), (11, 5), (9, 7), (7, 5), (9, 3), (7.4, 3.8), (7.4, 6.2), (10.4, 3.6), (10.6, 6.2), (20, 12), (20, 24), (22, 23.7), (24, 22.5), (24.4, 22), (25.6, 20.1), (26, 18), (25.6, 16), (24.4, 14), (24, 13.5), (22.1, 12.4), (17.9, 12.4), (15.9, 13.6), (15.2, 14.5), (14.3, 16), (14, 18), (14.4, 20), (15.5, 22), (16.3, 22.8), (25.2, 15), (14.8, 15), (19, 12.1), (23.3, 13), (25.9, 19), (14.1, 19.2), (14.1, 17), (15.1, 21.4), (17.4, 23.4), (18.6, 23.8), (21, 23.9), (23, 23.2), (24.9, 21.4), (25.4, 20.6), (6.2, 6), (6.6, 6.8), (8, 7.8), (9.9, 7.8), (10.5, 7.6), (11.2, 7), (11.6, 6.6), (11.7, 6.3), (11.8, 6), (11.9, 5.7), (12, 4.6), (11.9, 4.2), (11.8, 3.8), (11.6, 3.5), (10.5, 2.4), (8.2, 2.1), (7.4, 2.5), (6.1, 4.2), (8, 6.7), (7.2, 6), (7.1, 5.6), (7, 4.6), (7.1, 4.3), (7.7, 3.5), (8, 3.3), (8.3, 3.1), (9.5, 3.1), (10.8, 4.2), (10.8, 5.9), (9.8, 6.8)]

cl1 = Cluster("a",(11,23),2, '#1f77b4')
cl2 = Cluster("b",(8,5),0.5, '#2ca02c')
cl3 = Cluster("c",(12,9.5),3, '#17becf')

clusters = [cl1, cl2, cl3]

plot_state(clusters,points)
"""