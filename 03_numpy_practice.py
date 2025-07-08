import numpy as np

# 建立一維陣列
a = np.array([1, 2, 3, 4, 5])
print("一維陣列:", a)

# 建立二維陣列
b = np.array([[1, 2, 3], [4, 5, 6]])
print("二維陣列:\n", b)

# 建立全零、全一、隨機陣列
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
randoms = np.random.rand(2, 3)
print("全零陣列:\n", zeros)
print("全一陣列:\n", ones)
print("隨機陣列:\n", randoms)

# 陣列運算
c = np.array([10, 20, 30, 40, 50])
print("加法:", a + c)
print("乘法:", a * 2)
print("取平均:", np.mean(a))
print("取最大:", np.max(c))
