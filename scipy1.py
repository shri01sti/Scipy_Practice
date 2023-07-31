import scipy
import numpy as np
from scipy import constants
from scipy.optimize import root
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

from math import cos

'''
print(scipy.__version__)
#1 liter = cu.m?
print(constants.liter)
print(constants.pi)

#dir() func to see a list of all units under constants
print(dir(constants))


#Optimizes in Scipy: finds root of every non linear eqn
#finding root of a non linear eqn
# uses scipy.optimix=ze.root func
def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)  #uses root function with argument(func, initial guess)
print(myroot.x)  # prints only root 
print(myroot)    #prints all inf about the solution


#optimizes for finding minima
def eqn(x):
    return x**2 + x +2

my_min = minimize(eqn, 0, method = 'BFGS')
print(my_min)
print(my_min.x)

#finding maximum value
def eqn(x):
    return -(x**2 + x + 2)  # Negate the function to find maximum (since we're minimizing)

# Constraint: x should be between -10 and 10
constraint = {'type': 'ineq', 'fun': lambda x: x - (-10), 'jac': lambda x: 1,
              'type': 'ineq', 'fun': lambda x: 10 - x, 'jac': lambda x: -1}

my_max = minimize(eqn, x0=0, method='BFGS', constraints=constraint)

print(my_max)


#creating CSR(Compressed Sparse Row) matrix from an array
arr = np.array([0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

arr_view = np.array([[0,0,0], [0,0,1], [1,0,2]])
print(csr_matrix(arr_view).data)  # viwing stored dat(not zero items) using .data method

print(csr_matrix(arr_view).count_nonzero()) #counting non zero items

#eliminating zeros item
mat_elim = csr_matrix(arr_view)
mat_elim.eliminate_zeros()
print(mat_elim)

#eliminating duplicates by adding them
mat_sumdup = csr_matrix(arr_view)
mat_sumdup.sum_duplicates()
print(mat_sumdup)

#converting from csr to csc with tocsc()method
new_arr = csr_matrix(arr_view).tocsc()
print('csc form', new_arr)
'''

#finding connected components in adjacency matrix
arr = np.array([[0,1,2], [1,0,0], [2,0,0]])
new_arr = csr_matrix(arr)
print(connected_components(new_arr))

print('finding shortest path from element 1 to 2',dijkstra(new_arr, return_predecessors = True, indices = 0))

print('finding shortest path betwn all pair of elements',floyd_warshall(new_arr, return_predecessors = True))

print('finding shortest path from element 1 to 2 with a negative weight',bellman_ford(new_arr, return_predecessors = True, indices = 0))

#traverse the graph depth  and breadth first for given adjacency matrix
arr = np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,1,0],
    [0,1,0,1]
])
new_arr = csr_matrix(arr)
print('depth first order', depth_first_order(new_arr,1))

print('breadth first order', breadth_first_order(new_arr,1))

