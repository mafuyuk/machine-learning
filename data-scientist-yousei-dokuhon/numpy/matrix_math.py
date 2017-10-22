import numpy as np

a = np.arange(4).reshape(2,2)
print("a: \n{}".format(a))

b = np.arange(3,7).reshape(2,2)
print("b: \n{}".format(b))


print("a + b: \n{}".format(a + b))
print("a.T: \n{}".format(a.T))
print("a.T + b: \n{}".format(a.T + b))
print("a - b: \n{}".format(a - b))
print("np.dot(a,b): \n{}".format(np.dot(a,b)))