import numpy as np

a=np.arange(6).reshape(2,3)
print("a: \n{}".format(a))

b=np.arange(6,12).reshape(2,3)
print("b: \n{}".format(b))


print("np.c_[a,b]: \n{}".format(np.c_[a,b]))
print("np.r_[a,b]: \n{}".format(np.r_[a,b]))


# 1次元配列の場合
c=np.arange(3)
print("c: \n{}".format(c))

d=np.arange(3,6)
print("d: \n{}".format(d))

print("np.c_[c,d]: \n{}".format(np.c_[c,d]))
print("np.r_[c,d]: \n{}".format(np.r_[c,d]))