import numpy as np

# 2 * 2の行列作成
a = np.array([[1,2],[3,4]])
print("a: \n{}".format(a))

# サイズ10のベクトルを作成
b = np.arange(10)
print("b: \n{}".format(b))

# bを2*5行列に変形している
c = b.reshape(2,5)
print("c: \n{}".format(c))