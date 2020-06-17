import math

from schema import Cluster
from methods import get_distances, calcularNuevosCluster, assign_point
from plot_state import plot_state

def soft_clustering(points,clusters):
    i = 0
    
    while(i<20): 
        
        #Se recorren todo los puntos para calcular la distancia y clasificarlos
        for p in points:

            #Obtenemos los grados de pertenencia del punto <p> a los clusters
            gp = get_distances(p,clusters)

            #Asignamos el punto <p> a todos los clusters con su repectiva pertenencia
            assign_point(p,gp,clusters)
        
        #Se muestran los resultados en una gráfrica
        plot_state(clusters,points)

        #Se actualizan los radios y los centros
        clustersNuevos = calcularNuevosCluster(clusters)

        #Si los cluster no han cambiado del paso anterior, se continua el algoritmo
        i +=1

        
        
"""
points = [(9, 7), (7.7, 6.5), (7, 5), (11, 5), (9, 3), (10.3, 3.5), (7.3, 4), (10.3, 6.5), (3, 2), (2, 3), (1, 2), (2, 1), (1.2, 1.4), (1.2, 2.6), (2.7, 1.3), (2.8, 2.6)]

cl1 = Cluster("azul",(3,2.5),1,'#1f77b4')
cl2 = Cluster("verde",(8,4),2,'#2ca02c')

clusters = [cl1, cl2]

mirar si los puntos tienen forma de circunferencia
para calcular la media tener en cuenta los pesos:
    circunferencia: (p1 - xc)**2 + (p2 - yc)**2 = r**2
    cada 3 pts busca que sean una circunferencia

(calcular que todos los puntos del cluster pertenecen a la circunferecnia con una 
cota de error para que no sea exacto, si ese punto no lo cumple, se le asigna el 
siguiente cluster más cercano)
"""

points = [(9, 8), (7, 7.3), (6, 5), (12, 5), (9, 2), (11, 2.7), (6.4, 3.5), (11, 7.2), (11, 5), (9, 7), (7, 5), (9, 3), (7.4, 3.8), (7.4, 6.2), (10.4, 3.6), (10.6, 6.2), (20, 12), (20, 24), (22, 23.7), (24, 22.5), (24.4, 22), (25.6, 20.1), (26, 18), (25.6, 16), (24.4, 14), (24, 13.5), (22.1, 12.4), (17.9, 12.4), (15.9, 13.6), (15.2, 14.5), (14.3, 16), (14, 18), (14.4, 20), (15.5, 22), (16.3, 22.8), (25.2, 15), (14.8, 15), (19, 12.1), (23.3, 13), (25.9, 19), (14.1, 19.2), (14.1, 17), (15.1, 21.4), (17.4, 23.4), (18.6, 23.8), (21, 23.9), (23, 23.2), (24.9, 21.4), (25.4, 20.6), (6.2, 6), (6.6, 6.8), (8, 7.8), (9.9, 7.8), (10.5, 7.6), (11.2, 7), (11.6, 6.6), (11.7, 6.3), (11.8, 6), (11.9, 5.7), (12, 4.6), (11.9, 4.2), (11.8, 3.8), (11.6, 3.5), (10.5, 2.4), (8.2, 2.1), (7.4, 2.5), (6.1, 4.2), (8, 6.7), (7.2, 6), (7.1, 5.6), (7, 4.6), (7.1, 4.3), (7.7, 3.5), (8, 3.3), (8.3, 3.1), (9.5, 3.1), (10.8, 4.2), (10.8, 5.9), (9.8, 6.8)]

cl1 = Cluster("Azul",(11,23),2, '#1f77b4')
cl2 = Cluster("Verde",(8,5),0.5, '#2ca02c')
cl3 = Cluster("Rojo",(12,9.5),3, '#cf1717')

clusters = [cl1, cl2, cl3]

soft_clustering(points,clusters)
