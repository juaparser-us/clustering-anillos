import math

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

    return result

def distance(org,dest):
    return math.sqrt(pow(dest[0]-org[0],2)+pow(dest[1]-org[1],2))

""" Test the method to obtain the degree of belonging for a point
cl1 = ["a",(1,1),3]
cl2 = ["b",(5,4),2]
cl3 = ["c",(7,9),3.5]

clusters = [cl1, cl2, cl3]

p = (17,10)

print(get_belongings(p,clusters))
"""
