import math
import get_belongings from belonging
import distance from belonging
import get_circle from tp_extended

def soft-clustering(points,clusters):

#    m1 = a b d
#    m2 = c e
# No olvidar la condicion de parada del algoritmo

    #Crear x variables como x clusters haya
    # En el for, coger el cluster con el gp máximo, y añadir el punto a esa variable x
    for p in points:
        # Recorro los puntos y calculo el grado de pertenencia a cada cluster
        # creo las circunferencias en base a esas circunferencias
        gp = get_belongings(p,clusters)
        cp = max(gp)
        cp add p
    
    clusterNuevos = calcularNuevosCluster(clusters)

    si clustersAnterior = clusterNuevos
        fin algoritmo
    sino
        siguiente iteracion




""" Test the method to obtain the degree of membership for a point
cl1 = ["a",(1,1),3]
cl2 = ["b",(5,4),2]
cl3 = ["c",(7,9),3.5]

clusters = [cl1, cl2, cl3]

p = (17,10)

print(get_belongings(p,clusters))
"""