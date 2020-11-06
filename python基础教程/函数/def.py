#-----------------------------------
# 定义函数
#-----------------------------------

def change_list(param_list) :
    '改变列表类型的参数'
    param_list[0] = 'nothing'
    return param_list

x = ['a', 'b', 'c']
# 给函数传可变参数, 会改变原始变量
change_list(x)
print(x)

# 函数传参的过程相当于
x = ['a', 'b', 'c']
y = x
y[0] = 'nothing'
print(x)

# 防止原始变量被改变的做法
x = ['a', 'b', 'c']
change_list(x[:])
print(x)

# 这里要注意:
# python允许自定义的函数重名
# 后定义的函数会覆盖掉先定义的函数
def change_list(param_list) :
    print(param_list)

change_list(['a', 'b', 'c'])