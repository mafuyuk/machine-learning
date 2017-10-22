import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])

X,Y=np.meshgrid(x,y)
print("X.ravel(): \n{}".format(X.ravel()))
print("Y.ravel(): \n{}".format(Y.ravel()))