import numpy as np
import matplotlib.pyplot as plt
import math

def update_cluster(cluster):
    points = cluster.belonging
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    centroid = (sum(x) / len(points), sum(y) / len(points))

    x.append(centroid[0])
    y.append(centroid[1])

    xc = centroid[0]
    yc = centroid[1]

    m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points]
    r = np.mean(m)

    cluster.center = (xc,yc)
    cluster.radius = r
    cluster.belonging = []



