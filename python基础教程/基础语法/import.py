
#-----------------------------------
# 引入包
#-----------------------------------

# 直接调用时
# print(sqrt(5))
# NameError: name 'sqrt' is not defined

# 直接导入包中所有
import math
print(math.sqrt(2))

# 导入包中某个函数
from math import log10
print(log10(100))

# 导入包时重命名
import math as m
print(m.log(5, 2))

# 导入包中函数时重命名
from math import log as l
print(l(2, 5))