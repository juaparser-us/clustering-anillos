import numpy as np
import matplotlib.pyplot as plt
import math
from schema import Cluster

# Método para mostrar el estado inicial de cada ejecución del algoritmo
def initial_plot(clusters,points):

    __, ax = plt.subplots()

    ax.set(xlim=(0, 25), ylim = (0, 30))

    # Pintamos las circunferencias de cada cluster con sus respectivos colores
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

        #Añadimos los puntos (de color negro) a la gráfica
        for p in points:
            ax.scatter(p[0],p[1],color='#000000')

    plt.show()

# Método para mostrar el estado objetivo
# También está disponible para mostrar los estados por iteración
def plot_state(clusters, points):

    __, ax = plt.subplots()

    ax.set(xlim=(0, 30), ylim = (0, 25))

    # Pintamos las circunferencias de cada cluster con sus respectivos colores
    for c in clusters:
        belongings = c.belonging.keys()
        xc = c.center[0]
        yc = c.center[1]
        ax.scatter(xc,yc, marker="x", c=c.color)
        if(len(c.belonging)!=0):
            m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in c.belonging];
            r = np.mean(m)
        else:
            r = c.radius
        a_circle = plt.Circle((c.center[0], c.center[1]), r,fill=False,color=c.color)
        ax.add_artist(a_circle)

        # Aquí se añade los puntos asignados a cada cluster con los colores
        # de sus respectivos clusters
        for p in belongings:
            ax.scatter(p[0],p[1], c=c.color)

        """ PRUEBA DE DETECCIÓN DE RUIDO (No completado)  
        for d in c.noise:
            ax.scatter(d[0],d[1],c="#000000")
        """
  
    plt.show()
