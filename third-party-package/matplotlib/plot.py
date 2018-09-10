import numpy as np
import matplotlib.pyplot as plt

train = np.loadtxt('click.csv', delimiter=',', skiprows=1)
train_x = train[:,0]
train_y = train[:,1]

# plt.plot(train_x, train_y, 'o')
# plt.show()

# 標準化
mu = train_x.mean()
sigma = train_x.std()
def standardize(x):
  return (x - mu) / sigma

train_z = standardize(train_x)
plt.plot(train_z, train_y, 'o')
plt.show()