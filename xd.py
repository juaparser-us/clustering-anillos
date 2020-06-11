
import numpy as np
import matplotlib.pyplot as plt
import math

points = [(9, 7), (7.7, 6.5), (7, 5), (11, 5), (9, 3), (10.3, 3.5), (7.3, 4), (10.3, 6.5), (3, 2), (2, 3), (1, 2), (2, 1), (1.2, 1.4), (1.2, 2.6), (2.7, 1.3), (2.8, 2.6)]


x = [p[0] for p in points]
y = [p[1] for p in points]
centroid = (sum(x) / len(points), sum(y) / len(points))
x.append(centroid[0])
y.append(centroid[1])

xc = centroid[0];
yc = centroid[1];

m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points];

r = np.mean(m);

plt.scatter(x,y);
plt.show();

print(centroid)
