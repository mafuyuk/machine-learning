import numpy as np

a = np.arange(4).reshape(2,2)
print("a: \n{}".format(a))


v = np.array([10,20])
print("v: \n{}".format(v))
print("np.dot(a,v): \n{}".format(np.dot(a,v)))
print("np.dot(v,a): \n{}".format(np.dot(v,a)))