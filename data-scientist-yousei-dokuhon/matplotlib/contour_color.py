import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,200)
y=np.linspace(-5,5,200)

X,Y=np.meshgrid(x,y)
Z=X.ravel()**2-Y.ravel()**2
plt.contourf(X,Y,Z.reshape(X.shape))
plt.show()