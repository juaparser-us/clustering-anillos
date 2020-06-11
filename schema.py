#in ->  name: identifier of the cluster
#       center: center of the circunference
#       radius: radius of the circunference
#       bel: belongings of the point cloud for this cluster
class Cluster():

    def __init__(self,name,center,radius,bel):
        self.name = name
        self.center = center
        self.radius = radius
        self.belonging = bel
    
    def get_result(self):
        return [self.name,self.center,self.radius,self.belonging]

#in ->  num: iteration number
#       clusters: list of all cluster in this iteration
class Iteration():

    def __init__(self,num,clusters):
        self.num = num
        self.clusters = clusters
    
    def get_result(self):
        return {self.num:[self.clusters]}

""" Tests for the data structure

cl1 = Cluster("a",(1,1),4.1,[0.2,0.3,0.8,0.9])
cl2 = Cluster("b",(1,3),3.0,[0.6,0.5,0.1,0.05])
cl3 = Cluster("c",(4,2),2.5,[0.2,0.2,0.1,0.05])

cl4 = Cluster("a",(1,2),4.1,[0.2,0.3,0.8,0.9])
cl5 = Cluster("b",(1.5,3),3.0,[0.6,0.5,0.1,0.05])
cl6 = Cluster("c",(4.3,2.7),2.5,[0.2,0.2,0.1,0.05])

it1 = Iteration(1,[cl1,cl2,cl3])
it2 = Iteration(2,[cl4,cl5,cl6])
iterations = [it1,it2]

for x in iterations:
    print(x.get_result())
"""
