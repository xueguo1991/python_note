#-----------------------------------
# 传递参数 关键字参数
#-----------------------------------

# 自定义的形参在调用函数时, 是一个关键字
# 调用时可以忽略顺序, 有效避免未知参数的弊端
name = '唐僧'
position = '师傅'

# 定义参数时, 没有默认值的参数在前, 有默认值的参数在后
# def intro(param_position = '长老', param_name)
# SyntaxError: non-default argument follows default argument
def intro(param_name, param_position = '长老'):
    str = '在去往西天的路上, {name}是一位{position}.'
    print(str.format(name = param_name, position = param_position))

intro(param_position = position, param_name = name)
intro(param_name = name)