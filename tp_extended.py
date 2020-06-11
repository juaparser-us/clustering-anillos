import numpy as np
import matplotlib.pyplot as plt
import math

points = [(9, 7), (7.7, 6.5), (7, 5), (11, 5), (9, 3), (10.3, 3.5), 
            (7.3, 4), (10.3, 6.5)]

x = [p[0] for p in points]
y = [p[1] for p in points]
centroid = (sum(x) / len(points), sum(y) / len(points))
x.append(centroid[0])
y.append(centroid[1])

xc = centroid[0];
yc = centroid[1];

m = [math.sqrt(math.pow(xc-p[0],2) + math.pow(yc-p[1],2)) for p in points];

r = np.mean(m);

fig, ax = plt.subplots()

ax.set(xlim=(5, 15), ylim = (0, 10))

a_circle = plt.Circle((centroid[0], centroid[1]), r,fill=False)
ax.add_artist(a_circle);
ax.scatter(x,y);
plt.show();

print(centroid)
