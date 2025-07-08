# use_module.py

#import：匯入整個模組，使用模組內函式需要打完整，例如mymodule.add()
import mymodule

#from...import：只匯入模組中的某一個函式，使用時不需打mymodule.add()，可直接用add()呼叫
from mymodule import add 
print(add(3, 4))

#as：將模組名稱別名，使用時不需打mymodule.add()，可直接用別名mm.add()呼叫
import mymodule as mm
print(mm.add(3, 4))

x = 10
y = 5

print(f"{x} + {y} = {mymodule.add(x, y)}")
print(f"{x} - {y} = {mymodule.subtract(x, y)}")
print(f"{x} * {y} = {mymodule.multiply(x, y)}")
print(f"{x} / {y} = {mymodule.divide(x, y)}")
