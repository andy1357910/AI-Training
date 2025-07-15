import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# 載入資料
housing = fetch_california_housing()
X = housing.data
y = housing.target
feature_names = housing.feature_names

# 切分資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立隨機森林回歸模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 取得特徵重要性
importances = rf_model.feature_importances_

# 繪製條狀圖
plt.figure(figsize=(10,6))
plt.barh(range(len(importances)), importances, align='center')
plt.yticks(range(len(importances)), feature_names)
plt.xlabel("Feature Importance")
plt.title("Feature Importance in Random Forest (California Housing)")
plt.show()

# 顯示特徵與重要性數值
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")
