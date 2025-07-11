import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#載入資料
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

#切分資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#建立模型並訓練
model = LinearRegression()
model.fit(X_train, y_train)

#查看結果
print("權重 (係數):", model.coef_)
print("截距:", model.intercept_)
print("R^2 分數:", model.score(X_test, y_test))


# 預測
y_pred = model.predict(X_test)

# 計算殘差
residuals = y_test - y_pred

# 繪製殘差圖
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted Values")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residual Plot")
plt.show()

# 畫預測 vs 實際圖
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 對角線
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted (Linear Regression)")
plt.show()