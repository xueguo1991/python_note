#-----------------------------------
# 传递参数 收集关键字参数
#-----------------------------------
x = '孙行者'
y = '行者孙'
z = '沙僧'
w = '八戒'

def fourFolks(param_x, param_y, **four) :
    print(param_x, param_y)
    print(four)
# 关键字参数会被收集到一个字典中
# 关键字参数收集会忽略位置参数
fourFolks(x, y, z = z, w = w)