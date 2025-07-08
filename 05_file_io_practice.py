# 05_file_io_practice.py

# 建立並寫入檔案
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello, this is Andy.\n")
    f.write("This is your AI learning log.\n")

print("已寫入 sample.txt")

# 讀取檔案內容
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("讀取內容：")
print(content)

# 讀取檔案每行
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("逐行讀取：")
for line in lines:
    print(line.strip())
