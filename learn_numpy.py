import numpy as np

print('1次元配列を作る')
i_arr = np.asarray([1,2,3], dtype=np.int32)
print(i_arr)

print('配列の型を変更する')
f_arr = i_arr.astype(np.float32)
print(f_arr)

print('多次元配列を作る')
arr= np.asarray([[1,2,3], [4,5,6]])
print(arr)

print('配列の構造を見る')
print(arr.shape)

print('要素が全部0の配列')
print(np.zeros((2, 3)))

print('要素がすべて1の配列')
print(np.ones((2, 3)))

print('要素を[0-1)の範囲でランダムに初期化する')
print(np.random.rand(2, 3))

print('要素を正規分布にのっとって生成する')
print(np.random.randn(2, 3))


a = np.asarray([[1,2,3],[4,5,6]])
print('配列の')
print(3 * a)

b = np.asarray([1,2,3])
c = np.asarray([[4],[5],[6]])
print(b)
print(c)
print(b * c)
print(b.dot(c))

print('100の乱数生成')
arr = np.random.rand(100)
print(arr)

print('配列の平均')
print(np.mean(arr))

print('最大値')
print(np.max(arr))

print('最小値')
print(np.min(arr))

print('標準偏差')
print(np.std(arr))

print('和')
print(np.sum(arr))