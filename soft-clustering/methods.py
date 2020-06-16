import math
from schema import Cluster
import numpy as np
import matplotlib.pyplot as plt

def get_distances(p,clusters):
    
    belongings = []
    norm = 0
    for x in clusters:
        d = abs(distance(p,x.center)-x.radius)
        belongings.append((x,d))
        norm += d
    
    result = {}
    for x in belongings:
        result[x[0]]= (1-(x[1]/norm))/2
    
    return result

def assign_point(point,gp,clusters):
    max = (None,0)
    for c in clusters:
        if(max[1] == 0 or gp[c]>max[1]):
            max = (c,gp[c])
    max[0].assign(point,max[1])

"""
def get_distance(point,cluster):
    result = abs(distance(point,cluster.center)-cluster.radius)
    return result
"""
def distance(p0,p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def calcularNuevosCluster(clusters):
    for c in clusters:
        update_cluster(c)
    return clusters

def update_cluster(cluster):
    
    points = cluster.belonging
    print(points)
    print("Longitud: ",len(points))
    print()
    x = []
    y = []
    for k in points.keys():
        x.append(k[0]*points[k])
        y.append(k[1]*points[k])

    xc, yc = (sum(x) / len(points), sum(y) / len(points))
    """
    x.append(centroid[0])
    y.append(centroid[1])
    """
    m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points]
    r = np.mean(m)

    cluster.center = (xc,yc)
    cluster.radius = r
    cluster.belonging = {}

"""
cl1 = Cluster("azul",(20.876190476190477, 20.95238095238095),4.922205716383306, '#1f77b4')
cl2 = Cluster("verde",(7.687499999999999, 4.3166666666666655),1.816310104503276, '#2ca02c')
cl3 = Cluster("rojo",(13.644117647058826, 8.658823529411766),5.576984354132253, '#cf1717')
cl4 = Cluster("rojo",(15.644117647058826, 3.658823529411766),4.576984354132253, '#cf1717')
clusters = [cl1, cl2, cl3]

p = (11.2,7)

gp = get_distances(p,clusters)
assign_point(p,gp,clusters)

dic = {(1,2):0.8,(2,1):0.15}
x = []
y = []
for k in dic.keys():
    x.append(k[0]*dic[k])
    y.append(k[1]*dic[k])

print(x)
print(y)
xc, yc = (sum(x) / len(x), sum(y) / len(y))
print(xc,"-",yc)
"""
