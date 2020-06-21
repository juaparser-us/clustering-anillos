import math
from schema import Cluster
import numpy as np
import matplotlib.pyplot as plt
from plot_state import plot_state
import csv

# Método para leer archivos .csv
def import_csv(file):

    with open(file, newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        res = []
        for row in reader:
            res.append((float(row[0]),float(row[1])))
    
    return res

# Método que calcula los grados de pertenencia de un punto a todos los clusters
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

# Se asigna un punto a un cluster mediante el valor de su grado de pertenencia
def assign_point(point,gp,clusters):
    max = (None,0)
    for c in clusters:
        if(max[1] == 0 or gp[c]>max[1]):
            max = (c,gp[c])
    
    max[0].assign(point,max[1])
    
    """    PRUEBA DE LA DETECCIÓN DE RUIDO (No completado)    
    if(max[1] > 0.15):
        max[0].assign(point,max[1])
    else:
        max[0].noise.append(point)
    """

# Método que calcula la distancia entre dos puntos
def distance(p0,p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Se actualizan todos los clusters, usando el método siguiente
def calcularNuevosCluster(clusters):
    res = []

    for c in clusters:
        cl = update_cluster(c)
        res.append(cl)

    return res

# Actualiza los centros y los radios de un cluster
def update_cluster(cluster):
    
    points = cluster.belonging

    x = []
    y = []
    pond = []
    # Se calcula la media ponderada con los grados de pertenencia
    for k in points.keys():
        x.append(k[0]*points[k])
        y.append(k[1]*points[k])
        pond.append(points[k])

    xc, yc = (sum(x) / sum(pond), sum(y) / sum(pond))

    m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points]
    r = np.mean(m)

    res = Cluster(cluster.name,(xc,yc),r,cluster.color)

    return res

# Método para calcular que los puntos de un cluster pertenecen
# a una circunferencia (NO COMPLETADO)
"""
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
"""
# Método para ordenar la lista de puntos por distancia usando el 
# algoritmo burbuja (NO COMPLETADO)
"""
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
"""

# Método que genera aleatoriamente nubes de punto con forma de circunferencias 
# eligiendo el número de circunferencias y los puntos para cada una
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

    # Se comprueba que el punto aleatorio pertenece al perímetro de la circunferencia
    random = 0
    for c in cir:
        random = 0
        while(random<nps):
            x = round(np.random.uniform(0,23),3)
            y = round(np.random.uniform(0,28),3)

            ec = (x - c[0])**2 + (y - c[1])**2 
            r = cir[c]
            # Se compara con la ecuación de la circunferencia y si coincide,
            #  se escoge ese punto
            if((ec > (r**2)-0.1) and (ec < (r**2)+0.1) and (x not in res_x) and (y not in res_y)):
                res_x.append(x)
                res_y.append(y)
                random += 1
    
    for i in range(len(res_x)):
        res.append((res_x[i],res_y[i]))

    # Aquí se representa la nube de puntos obtenida
    __, ax = plt.subplots()
    ax.set(xlim=(0, 25), ylim = (0, 30))

    plt.plot(res_x,res_y,'o',markersize=2)
    plt.show()
    
    return res
