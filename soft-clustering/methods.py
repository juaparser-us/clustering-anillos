import math
from schema import Cluster
import numpy as np
import matplotlib.pyplot as plt
from plot_state import plot_state
import csv

def import_csv(file):

    with open(file, newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        res = []
        for row in reader:
            res.append((float(row[0]),float(row[1])))
    
    return res

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

def distance(p0,p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def calcularNuevosCluster(clusters):
    res = []

    for c in clusters:
        cl = update_cluster(c)
        res.append(cl)

    return res

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

    m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points]
    r = np.mean(m)

    res = Cluster(cluster.name,(xc,yc),r,cluster.color)

    return res

def comprobar_radio(cluster):

    puntos = list(cluster.belonging.keys())
    points = bubbleSort(puntos)
    punto = points[0]
    ant = (punto,distance(punto,cluster.center))
    points.remove(punto)

    lista = []

    for p in points:
        d = (p,distance(p,cluster.center))
        diff = abs(ant[1]-d[1])

        if(diff>0.2):
            lista.append(d[0])
            del cluster.belonging[d[0]]
        else:
            ant = d
        
       
    return lista

def bubbleSort(lista):

    n = len(lista)
    points = lista
    result = [lista[0]]
    points.remove(result[0])
    i = 0

    while(i<n-1):
        dist_ant = (0,0)
        n2 = len(points)
        
        for j in range(n2):
            d = distance(result[i],points[j])            
            if (d<dist_ant[1] or dist_ant[1] == 0):
                dist_ant = (points[j],d)

        if(dist_ant[0] != 0):
            result.append(dist_ant[0])

        points.remove(result[i+1])
        i += 1

    return result

def get_tests_points(nc,nps):
    cir = {}

    #Obtenemos el número de circunferencias que queremos
    for i in range(nc):
        x = round(np.random.uniform(0,15),3)
        y = round(np.random.uniform(0,20),3)
        r = round(np.random.uniform(0,8),3)
        cir[(x,y)] = r

    res = []
    res_x = []
    res_y = []

    random = 0
    for c in cir:
        random = 0
        while(random<nps):
            x = round(np.random.uniform(0,23),3)
            y = round(np.random.uniform(0,28),3)

            ec = (x - c[0])**2 + (y - c[1])**2 
            r = cir[c]

            if((ec > (r**2)-0.1) and (ec < (r**2)+0.1) and (x not in res_x) and (y not in res_y)):
                res_x.append(x)
                res_y.append(y)
                random += 1
    
    for i in range(len(res_x)):
        res.append((res_x[i],res_y[i]))

    __, ax = plt.subplots()
    ax.set(xlim=(0, 25), ylim = (0, 30))

    plt.plot(res_x,res_y,'o',markersize=2)
    plt.show()
    
    return res

# TESTING -----------------------------------------------------------------------------------
"""
cl1 = Cluster("azul",(20.876190476190477, 20.95238095238095),4.922205716383306, '#1f77b4')
cl2 = Cluster("verde",(9.658842682776278, 5.121325523600608),2.5272781901055117, '#2ca02c')
cl3 = Cluster("rojo",(13.644117647058826, 8.658823529411766),5.576984354132253, '#cf1717')
clusters = [cl1, cl2, cl3]

p = (9,8)

gp = get_distances(p,clusters)
assign_point(p,gp,clusters)

near_cluster(cl2)
near_cluster(cl1)

dic = {(1,2):0.8,(2,1):0.15}
x = []
y = []
for k in dic.keys():
    x.append(k[0]*dic[k])
    y.append(k[1]*dic[k])

dic = {(1,2):0.8,(2,1):0.15}
p = list(dic.keys())[0]
del dic[p]
print(dic)
( 8.487809590880826 , 4.94469122298428 )
2.5352548921005265

center = (8.487809590880826, 4.94469122298428)
p1 = (7,7.3)
p2 = (8,7.8)
p3 = (9,7)
p4 = (9.8,6.8)

print(distance(p1,center))
print(distance(p2,center))
print("Diff: ",abs(distance(p1,center)-distance(p2,center)))
print(distance(p3,center))
print("Diff: ",abs(distance(p2,center)-distance(p3,center)))
print(distance(p4,center))
print("Diff: ",abs(distance(p2,center)-distance(p4,center)))


cl3 = Cluster("Rojo",(8.487809590880826, 4.94469122298428),2.5352548921005265, '#cf1717')
clusters = [cl3]
points = {(7, 7.3): 0.4898448238792652, (6, 5): 0.4984003895632626, (9, 2): 0.48479580574633474, (6.4, 3.5): 0.49988091281836766, (11, 5): 0.49901508129061906, (9, 7): 0.4808137650678761, (10.4, 3.6): 0.49223693157126824, (10.6, 6.2): 0.4963245607552876, (6.2, 6): 0.4994236960219641, (6.6, 6.8): 0.495666729923895, (8, 7.8): 0.4836882665719938, (8.2, 2.1): 0.48943613507370826, (7.4, 2.5): 0.49544440425992986, (6.1, 4.2): 0.498875799052121, (9.5, 3.1): 0.4840837142832339, (10.8, 4.2): 0.4956299141697104, (10.8, 5.9): 0.49844381912758096, (9.8, 6.8): 0.48762839211439934}
cl3.belonging = points

sort = sorted(points , key=lambda k: [k[1], k[0]])
print(sort)
fig, ax = plt.subplots()
ax.set(xlim=(0, 30), ylim = (0, 25))

for p in sort:
    ax.scatter(p[0],p[1])
plt.show()


print("LONGITUD: ",len(points.keys()))
res = comprobar_radio(cl3)
print(res)
print()
ps = cl3.belonging
print(ps)

plot_state(clusters,list(ps.keys()))

print(cl3.center,"-",cl3.radius)

update_cluster(cl3)

print(cl3.center,"-",cl3.radius)
"""

