import math
from schema import Cluster

"""
def get_belongings(p,clusters):
    belongings = []
    norm = 0
    for x in clusters:
        d = abs(distance(p,x.center)-x.radius)
        belongings.append((x.name,d))
        norm += d
    
    result = []
    for x in belongings:
        result.append((x[0],x[1]/norm))
    
    return belongings
"""


def get_distance(point,cluster):
    result = abs(distance(p,x.center)-x.radius)
    return result

def distance(p0,p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


cl1 = Cluster("azul",(20.876190476190477, 20.95238095238095),4.922205716383306, '#1f77b4')
cl2 = Cluster("verde",(7.687499999999999, 4.3166666666666655),1.816310104503276, '#2ca02c')
cl3 = Cluster("rojo",(13.644117647058826, 8.658823529411766),5.576984354132253, '#cf1717')

clusters = [cl1, cl2, cl3]

p = (11.2,7)

print(get_belongings(p,clusters))
"""
v = get_belongings(p,clusters)[1]
r = get_belongings(p,clusters)[2]

print(v[0],v[1]," - ",cl2.radius," = ",abs(v[1]-1.816310104503276))
print(r[0],r[1]," - ",cl3.radius," = ",abs(r[1]-5.576984354132253))
"""

d = abs(distance(cl2.center,cl3.center))

print("Distancia entre rojo y verde (centros): ",d)
print("Suma de los radios de rojo y verde: ",cl2.radius+cl3.radius)