import scipy
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

'''
#Triangulation
points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
   
])
simplices = Delaunay(points).simplices  #simplices property creates a generalization of the triangle
plt.triplot(points[:,0], points[:,1], simplices)
plt.scatter(points[:,0], points[:,1], color = 'r')

plt.show()

#ConvexHull
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)   #Calculate the convex hull of the points using ConvexHull:

hull_points = hull.simplices  #Extract the indices of the points that form the hull:

plt.scatter(points[:,0],points[:,1])  #Create a scatter plot of the original points:

for simplex in hull:   #Plot the edges of the convex hull using the indices of hull points:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()
'''

#KDTrees
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
result = kdtree.query((1,1))
print(result)

#distance matrix: Euclidean Matrix
p1 = (1,0)
p2 = (10,2)
b1 = (True, False, True)
b2 = (False, True, True)
result = euclidean(p1,p2)
print('Euclidean distance',result)

print('Cityblock distance',cityblock(p1,p2))

print('Cosine distance',cosine(p1,p2))

print('hamming distance',hamming(b1,b2))