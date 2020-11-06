#-----------------------------------
# 传递参数 位置参数
#-----------------------------------
x = 100
y = 200
z = 300

# 跟参数的顺序直接相关
def plus(param_z, param_x = 5):
    print('{} + {} = {}'.format(param_z, param_x, param_z + param_x))
    return x + z

plus(z, x)
plus(y)