import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

# データの読み込み
iris = datasets.load_iris()

# 種類が2種類のものを試す
data = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

# ロジスティック回帰による学習と交差検定による評価
logi = LogisticRegression()
scores = cross_validation.cross_val_score(logi, data, target, cv = 5)

# 結果を表示する
print(scores)