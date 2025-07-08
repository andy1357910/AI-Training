import pandas as pd

# 建立資料
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}

# 建立 DataFrame
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 查看描述統計
print("\n描述統計:")
print(df.describe())

# 篩選資料
print("\n篩選 Age > 25:")
# df["Age"] > 25：產生一個 bool 序列，3筆資料bool為
# 0    False
# 1     True
# 2     True

# df[bool]：把布林值為 True 的列 篩選出來。
#       Name  Age  Score
# 1      Bob   30     90
# 2  Charlie   35     95

# 並print出來
print(df[df["Age"] > 25]) 

# 新增欄位
df["Pass"] = df["Score"] >= 90
print("\n新增 Pass 欄位:")
print(df)
