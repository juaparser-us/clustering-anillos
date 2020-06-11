import laspy
import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import path

points = [(9, 7), (7.7, 6.5), (7, 5), (11, 5), (9, 3), (10.3, 3.5), 
            (7.3, 4), (10.3, 6.5), (3, 2), (2, 3), (1, 2), (2, 1), (1.2, 1.4), 
            (1.2, 2.6), (2.7, 1.3), (2.8, 2.6)]

x = [p[0] for p in points]
y = [p[1] for p in points]

# Grab a numpy dataset of our clustering dimensions:
dataset = np.vstack([x, y]).transpose()
dataset.shape

def frange(start, stop, step):
  i = start
  while i < stop:
    yield i
    i += step
#ground points grid filter
n = 100 #grid step
xstep = (dataset[:, 0].max() - dataset[:, 0].min())/n
ystep = (dataset[:, 1].max() - dataset[:, 1].min())/n
for x in frange (dataset[:, 0].min(), dataset[:, 0].max(), xstep):
  for y in frange (dataset[:, 1].min(), dataset[:, 1].max(), ystep):
    datasetfiltered = dataset[(dataset[:,0] > x)
                             &(dataset[:, 0] < x+xstep)
                             &(dataset[:, 1] > y)
                             &(dataset[:, 1] < y+ystep)]

dataset = preprocessing.normalize(dataset)
clustering = DBSCAN(eps=2, min_samples=5, leaf_size=30).fit(dataset)

core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
core_samples_mask[clustering.core_sample_indices_] = True
labels = clustering.labels_
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

# Black removed and is used for noise instead.
fig = plt.figure(figsize=[100, 50])
ax = fig.add_subplot(111, projection='3d')
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
  for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
  if k == -1:
    # Black used for noise.
    col = [0, 0, 0, 1]
  class_member_mask = (labels == k)
  xy = dataset[class_member_mask & core_samples_mask]
  ax.scatter(xy[:, 0], xy[:, 1], c=col, marker=".")
plt.show()