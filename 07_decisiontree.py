from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. 載入資料
iris = load_iris()
X = iris.data
y = iris.target

# 2. 切分資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 建立決策樹模型
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. 預測與計算準確率
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"模型準確率：{acc:.2f}")

# 5. 可視化決策樹

# 設定畫布大小（12 x 8 吋）
plt.figure(figsize=(12, 8))


#plot_tree()參數如下：
# model
# ➔ 你訓練好的決策樹模型（DecisionTreeClassifier 物件）

# filled=True
# ➔ 讓節點用顏色區分類別，幫助更容易閱讀

# feature_names
# ➔ 顯示特徵名稱（例如花瓣長度、花瓣寬度等）

# class_names
# ➔ 顯示類別名稱（例如 setosa, versicolor, virginica）
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title("Decision Tree for Iris Dataset")
plt.show()
