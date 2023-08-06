import numpy as np
import scipy
from scipy import io
from scipy.interpolate import  interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe
from scipy.stats import skew, kurtosis
from scipy.stats import normaltest

'''
#export array as varname 'vec' to a matfile
arr = np.arange(10)
io.savemat('arr.mat', {'vec': arr})

#import data from matlab format
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

print(mydata)

print(mydata['vec'])  #display only the array from the matlab data, result will create 2D create with increase of 1D
#to resolve this
mydata = io.loadmat('arr.mat', squeeze_me = True)
print(mydata['vec'])


#Scipy Interpolation
#interpolating values from 2.1, 2.2,.....2.9 for given xs and ys

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs,ys)   #interpled() func to interpolate a distribution with 1 variable
new_arr = interp_func(np.arange(2.1, 3, 0.1))  #substituting value of xs from (2.1 - 3) at an interval of 0.1
print('1D Interpolationn',new_arr)

#UnivariateSpline function
x1 = np.arange(10)
y1 = x1**2 + np.sin(x1) + 1

interp_func = UnivariateSpline(x1, y1)
new_arr = interp_func(np.arange(2.1,3,0.1))
print('Spline Interpolation',new_arr)

interp_func = Rbf(x1,y1)
new_arr = interp_func(np.arange(2.1,3,0.1))
print('interpolation with radial basis function',new_arr)
'''

#Statistical SIgnificance Test
v1 = np.random.normal(size = 1000)
v2 = np.random.normal(size = 1000)

result = ttest_ind(v1,v2)
print(result)  #result contains test statistic and pvalue
#test statistic measures diff betw the means of two samples

result_pval = ttest_ind(v1,v2).pvalue  #to return only p-value
print(result_pval)

#KS test
v = np.random.normal(size = 100)
res = kstest(v,'norm')

print(res)

print('Statistical  Description', describe(v))  #showing statistical description

print('Normality Test, Skewness',skew(v))

print('Normality Test, Kurtosis',kurtosis(v))

print('whether data comes from a normal distribution or not',normaltest(v))





