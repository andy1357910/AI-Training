# 資料型態練習範例

# 整數 (int)
a = 10
print("a 的值:", a)
print("a 的型態:", type(a))

# 浮點數 (float)
b = 3.14
print("b 的值:", b)
print("b 的型態:", type(b))

# 字串 (str)
c = "Hello, Andy!"
print("c 的值:", c)
print("c 的型態:", type(c))

# 布林值 (bool)
d = True
print("d 的值:", d)
print("d 的型態:", type(d))

# 列表 (list)
# 特性：有序、可變動（可增刪改）、允許重複元素
# 語法：用中括號 [] 包起來
# 用途：存放一組有序資料，且可能會經常變動
e = [1, 2, 3, 4, 5]
print("e 的值:", e)
print("e 的型態:", type(e))

# 元組 (tuple)
# 特性：有序、不可變（元素不能被修改）、允許重複
# 語法：用小括號 () 包起來
# 用途：存放不會變動的資料，像座標、設定參數等
f = (10, 20, 30)
print("f 的值:", f)
print("f 的型態:", type(f))

# 字典 (dict)
# 特性：無序、鍵值對（key-value）形式、鍵是唯一的、可變
# 語法：用大括號 {}，裡面是 key: value 配對
# 用途：用來存放結構化資料，比如學生姓名對應分數
g = {"name": "Andy", "age": 25}
print("g 的值:", g)
print("g 的型態:", type(g))

# 集合 (set)
# 特性：無序、不重複元素、可變
# 語法：用大括號 {}，但只有值沒有 key
# 用途：快速做元素去重、集合運算（交集、聯集、差集）
h = {1, 2, 3, 4, 5}
print("h 的值:", h)
print("h 的型態:", type(h))