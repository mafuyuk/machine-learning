import numpy as np

v = np.arange(10,15)
print("v: \n{}".format(v))

# インデックス2,3に当たる要素の取り出し
ii = np.array([2,3])
print("ii: \n{}".format(ii))

print("v[ii]: \n{}".format(v[ii]))


w = np.array([False,False,False,True,True])
print("w: \n{}".format(w))

# bool型の配列をインデックスに与えるとTrueに当たる要素だけ取り出す
print("v[w]: \n{}".format(v[w]))