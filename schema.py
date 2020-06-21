#Estructura de datos

class Cluster():

    def __init__(self,name,center,radius,color):
        self.name = name
        self.center = center
        self.radius = radius
        self.belonging = {}
        self.color = color
        #self.noise = [] PRUEBA DE LA DETECCIÓN DE RUIDO (No completado)
    
    def get_result(self):
        return [self.name,self.center,self.radius,self.belonging]
    
    def assign(self,point,gp):
        self.belonging[point] = gp
