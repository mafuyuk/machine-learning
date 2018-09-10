import numpy as np

a = np.arange(16).reshape(4,4)
print("a: \n{}".format(a))

# インデックスが1以上3未満の要素を新たな配列として取り出す
print("a[1,1]: \n{}".format(a[1:3]))

# 1行目を取り出す
print("a[1,:]: \n{}".format(a[1,:]))

# 1列目を取り出す
print("a[:,1]: \n{}".format(a[:,1]))