from scipy import sparse
import numpy as np

# lil_matrixは値の設定をするときに便利、計算には向かない
# csr_matrixとcsc_matrixは計算が早いが、値の設定に向かない
# csr_matrixは指定した行を取り出すのが高速
# csc_matrixは指定した列を取り出すのが高速

a=sparse.lil_matrix((5,5))
print("a.todense(): \n{}".format(a.todense()))

a[0,0] = 1;
a[1,2] = 2;
a[3,4] = 3;
a[4,4] = 4;
print("a.todense(): \n{}".format(a.todense()))

b=a.tocsr()
print("b.getrow(1).todense(): \n{}".format(b.getrow(1).todense()))


v=np.array([1,2,3,4,5])
print("a.dot(v): \n{}".format(a.dot(v)))