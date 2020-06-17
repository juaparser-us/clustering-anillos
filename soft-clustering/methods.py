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

#tener en cuenta si está dentro de la circunferencia
def near_cluster(cluster):
    for p in cluster.belonging:
        d = abs(distance(p,cluster.center)-cluster.radius)
        if(d>0.3):
            re_assign(point,gp)

"""
(p1 - xc)**2 + (p2 - yc)**2 = r**2
def assign_point(point,gp,clusters):
    for c in clusters:
        c.assign(point,gp[c])
"""
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

    x = []
    y = []
    pond = []
    for k in points.keys():
        x.append(k[0]*points[k])
        y.append(k[1]*points[k])
        pond.append(points[k])

    xc, yc = (sum(x) / sum(pond), sum(y) / sum(pond))
    """
    x.append(centroid[0])
    y.append(centroid[1])
    """
    m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points]
    r = np.mean(m)
    print("(",xc,",",yc,")")
    print(r)
    print()
    cluster.center = (xc,yc)
    cluster.radius = r
    cluster.belonging = {}


cl1 = Cluster("azul",(20.876190476190477, 20.95238095238095),4.922205716383306, '#1f77b4')
cl2 = Cluster("verde",(9.658842682776278, 5.121325523600608),2.5272781901055117, '#2ca02c')
cl3 = Cluster("rojo",(13.644117647058826, 8.658823529411766),5.576984354132253, '#cf1717')
clusters = [cl1, cl2, cl3]

p = (9,8)

gp = get_distances(p,clusters)
assign_point(p,gp,clusters)

near_cluster(cl2)
near_cluster(cl1)
"""
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
