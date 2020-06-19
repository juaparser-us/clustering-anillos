from methods import import_csv, get_tests_points
from soft_clustering import soft_clustering
from schema import Cluster
import numpy as np

"""
# input
print("Elige la opción deseada: ")
print("1) Nube de puntos aleatoria")
print("2) Nube de puntos importada desde un .csv")
input1 = int(input()) 
  
if (input1 == 1):

    points = get_tests_points(3,70)

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

if(input1 == 2):

    print("Escribe el nombre del fichero:")
    print("2_circunf.csv")
    print("3_conc.csv")
    input2 = input()
    print("Y también escriba el número de clústers:")
    input3 = int(input())
"""
points = import_csv("2_circunf.csv")
"""
    if(input3 == 3):
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

    if(input3 == 2):
"""
cl1 = Cluster("Azul",(1.8,4),1.5, '#1f77b4')
cl2 = Cluster("Verde",(13,9.2),2, '#2ca02c')
clusters = [cl1, cl2]

soft_clustering(points,clusters)
