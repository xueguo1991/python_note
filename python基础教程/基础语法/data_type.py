#-----------------------------------
# python 所有数据类型
#-----------------------------------

# 字符串
var_str = '我是一个字符串'
print(type(var_str))

# 整数
var_int = 1001
print(type(var_int))

# 浮点数
var_float = 10.12345
print(type(var_float))

# 数组
var_list = [
    1, 2, 3, 'a', 'b', 'c',
    ['d', 'e', 'f'],
    {'c': 'e', 15: '123'}
]
print(type(var_list))

# 元组
var_tuple = (1, 2, 3, 'a', 'b', 'c')
print(type(var_tuple))

# 字典
var_dict = {
    'a': '123', 'b': 456,
    (1, 'a'): '123'
}
print(type(var_dict))

# 空
var_none = None
print(type(var_none))
