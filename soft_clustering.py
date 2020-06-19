import math
import time
from schema import Cluster
from methods import get_distances, calcularNuevosCluster, assign_point, comprobar_radio, delete_noise
from plot_state import plot_state, initial_plot


def soft_clustering(points,clusters):
    i = 0
    j = 0
    z = 0
    ac = 0
    ant = clusters
    fin = False
    start_time = time.time()

#   initial_plot(clusters,points)

    while(not fin): 
        it_time = time.time()
        
        #Se recorren todo los puntos para calcular la distancia y clasificarlos
        for p in points:

            #Obtenemos los grados de pertenencia del punto <p> a los clusters
            gp = get_distances(p,ant)

            #Asignamos el punto <p> a todos los clusters con su repectiva pertenencia
            assign_point(p,gp,ant)

        if(z==1):
            plot_state(ant,points)

        #Se actualizan los radios y los centros
        res = calcularNuevosCluster(ant)

        i += 1

        print("Iteración",i,"===========================================================")
        if(z==0):
            ac = ac + (time.time() - it_time)
        print("Tiempo de iteración: ", (time.time() - it_time))
        print("Número de clusters: ",len(clusters))
        print("Centros y radios: ")
        for c in res:
            print(c.name,": ",c.center," [",c.radius,"]")
        print()

        #Si los cluster no han cambiado del paso anterior, se continua el algoritmo
        for n in range(len(res)):
            if((abs(res[n].center[0] - ant[n].center[0]) < 0.01) and 
                (abs(res[n].center[1] - ant[n].center[1]) < 0.01) and 
                (abs(res[n].radius - ant[n].radius) < 0.001)):
                j += 1

        ant = res

        if(z == 1):
            fin = True

        if(j == len(res)):
            z = 1
        
        j = 0

    #Se muestran los resultados en una gráfrica
    if(fin):
        print("=======================================================================")
        print("FIN DEL ALGORITMO")
        print("TIEMPO DE EJECUCIÓN: ", ac)
        print("=======================================================================")

