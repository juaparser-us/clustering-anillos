from methods import import_csv, get_tests_points
from soft_clustering import soft_clustering
from schema import Cluster
import numpy as np


# Uso interactivo del alogitmo mediante la consola
print("Elige la opción deseada: ")
print("1) Nube de puntos aleatoria con 3 clusters aleatorios")
print("2) Nube de puntos importada desde un .csv")
input1 = int(input()) 
  
if (input1 == 1):
    points = get_tests_points(3,100)

    cl1 = Cluster("Azul",
        (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
        round(np.random.uniform(0,8),3), '#1f77b4')
    cl2 = Cluster("Verde",
        (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
        round(np.random.uniform(0,8),3), '#2ca02c')
    cl3 = Cluster("Rojo",
        (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
        round(np.random.uniform(0,8),3), '#cf1717')

    clusters = [cl1, cl2, cl3]

if(input1 == 2):

    print("Escribe el nombre del fichero:")
    print("2_circunf.csv")
    print("3_conc.csv")
    input2 = input()

    points = import_csv(input2)

    if(input2 == "3_conc.csv"):
        cl1 = Cluster("Azul",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#1f77b4')
        cl2 = Cluster("Verde",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#2ca02c')
        cl3 = Cluster("Rojo",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#cf1717')
        clusters = [cl1, cl2, cl3]

    if(input2 == "2_circunf.csv"):
        cl1 = Cluster("Azul",(3,10),3, '#1f77b4')
        cl2 = Cluster("Verde",(17,6.5),4, '#2ca02c') #(9,5)
        clusters = [cl1, cl2]
    else:
        #Aqui se puede introducir manualmente el número de clústeres que se quiere si es para
        #importar un csv personalizado
        cl1 = Cluster("Azul",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#1f77b4')
        cl2 = Cluster("Verde",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#2ca02c')
        cl3 = Cluster("Rojo",
            (round(np.random.uniform(0,15),3),round(np.random.uniform(0,20),3)),
            round(np.random.uniform(0,8),3), '#cf1717')
        clusters = [cl1, cl2, cl3]

soft_clustering(points,clusters)
