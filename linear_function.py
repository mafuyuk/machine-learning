import numpy as np

theta0 = np.random.rand()
theta1 = np.random.rand()

# 予測関数
def f(x):
  return theta0 + theta1 * x

# 目的関数
def E(x, y):
  return 0.5 * np.sum((y - f(x)) ** 2)