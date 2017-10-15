import pandas as pd
import numpy as np

#Create a index
dates = pd.date_range("20130101", periods=6)

#Create a DatFrame
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns = list("ABCD"))

df2 = pd.DataFrame({
  'A' : 1.,
  'B' : pd.Timestamp('20130102'),
  'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
  'D' : np.array([3] * 4,dtype='int32'),
  'E' : pd.Categorical(["test","train","test","train"]),
  'F' : 'foo'
})


print(df)

print(df2.dtypes)

print('統計量の概要をまとめて表示')
print(df.describe())

print('DataFrameの行列を反転')
print(df.T)

# 任意の軸でソートをかける。
print('ラベルを降順でソート')
print(df.sort_index(axis=1, ascending=False))

print('データを選び出す')
print(df.loc['20130102':'20130104',['A','B']])


#Grouping and then calculate sum
df2 = pd.DataFrame({
  "A" : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
  "B" : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
  "C" : np.random.randn(8),
  "D" : np.random.randn(8)
})
print(df2.groupby('A').sum())