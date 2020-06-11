import numpy as np
import matplotlib.pyplot as plt

print("Input three coordinate of the circle:")
puntos1 = [(9, 7), (7.7, 6.5), (7, 5), (11, 5), (9, 3), (10.3, 3.5), 
            (7.3, 4), (10.3, 6.5), (3, 2), (2, 3), (1, 2), (2, 1), (1.2, 1.4), 
            (1.2, 2.6), (2.7, 1.3), (2.8, 2.6)]

x = []
y = []
for a in puntos1:
    x.append(a[0]);
    y.append(a[1]);
    
c = (x1-x2)**2 + (y1-y2)**2;
a = (x2-x3)**2 + (y2-y3)**2;
b = (x3-x1)**2 + (y3-y1)**2;
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) ;
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s;
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s ;
ar = a**0.5;
br = b**0.5;
cr = c**0.5 ;
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5;
print("Radius of the said circle:");
print("{:>.3f}".format(r));
print("Central coordinate (x, y) of the circle:");
print("{:>.3f}".format(px),"{:>.3f}".format(py));

x = [x1,x2,x3,px];
y = [y1,y2,y3,py];

plt.scatter(x, y);
plt.show();

