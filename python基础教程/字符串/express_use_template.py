#-----------------------------------
# 字符串格式设置 使用字符串模板
#-----------------------------------

import string

tmp = string.Template("我的编号是$no 我的营业额是：$money")
res = tmp.substitute(no = '00101', money = 15.88)
# 字符串模板使用关键字参数实现替换
print(res)