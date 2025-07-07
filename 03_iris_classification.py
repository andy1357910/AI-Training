from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# 載入鳶尾花資料集
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print("前5筆資料：")
print(df.head())

# 分割訓練集與測試集
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立KNN模型
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 預測
y_pred = model.predict(X_test)

# 評估準確率
acc = accuracy_score(y_test, y_pred)
print(f"模型準確率：{acc:.2f}")
