import numpy as np

# 行列やベクトルのすべての要素に同じ計算ができる

a=np.arange(4).reshape(2,2)
print("a: \n{}".format(a))

print("a*2: \n{}".format(a*2))


print("np.exp(a): \n{}".format(np.exp(a)))

# 行列のすべての要素に作用させる関数をユニバーサル関数という
# expはユニバーサル関数


print("a<2: \n{}".format(a<2))
print("a[a<2]: \n{}".format(a[a<2])) # インデクシングとの組み合わせ