from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# 載入鳶尾花資料集
iris = load_iris()
# iris的資料結構如下：
# iris = {'data': array([[5.1, 3.5, 1.4, 0.2],
#                [4.9, 3.0, 1.4, 0.2],
#                ...
#                [5.9, 3.0, 5.1, 1.8]]),
#  'target': array([0, 0, 0, ..., 2, 2, 2]),
#  'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'),
#  'DESCR': 'Iris Plants Database\n...',
#  'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
#  'filename': '.../iris.csv'}


#將 iris.data（150 筆花的長度寬度）+ 欄位名稱轉成可閱讀表格(DataFrame)。
df = pd.DataFrame(iris.data, columns=iris.feature_names)
#在 DataFrame 加上 target 欄位（0/1/2）。
df['target'] = iris.target 
print("前5筆資料：")
print(df.head())

# 分割訓練集與測試集
X = iris.data  #shape(150,4)，150筆資料，每筆資料有4個特徵
y = iris.target #shape(150,)，150筆資料，每筆資料有1種特徵(0、1、2)

# 把資料分成訓練集與測試集，test_size=0.2 將分成 8：2，random_state(任一整數)是為了讓每次執行程式(run)的訓練資料統一
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立KNN模型
# 建立 KNN 分類器物件，設定 k=3（使用最近的 3 個鄰居來判斷類別）。
model = KNeighborsClassifier(n_neighbors=3)
#  使用訓練集資料（特徵和答案）訓練模型，讓模型學習如何從特徵預測標籤。
model.fit(X_train, y_train)

# 預測
# 用已訓練好的模型，對測試集（X_test）進行預測，產生預測結果 y_pred（預測的花的品種）。
y_pred = model.predict(X_test)

# 評估準確率
# 計算模型預測結果 y_pred 與測試集正確標籤 y_test 的準確率。
acc = accuracy_score(y_test, y_pred)
print(f"模型準確率：{acc:.2f}")
