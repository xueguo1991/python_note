#-----------------------------------
# python 所有数据类型
#-----------------------------------

# 字符串 str
var_str = '我是一个字符串'
print(type(var_str))

# 整数 int
var_int = 1001
print(type(var_int))

# 浮点数 float
var_float = 10.12345
print(type(var_float))

# 列表 list
var_list = [
    1, 2, 3, 'a', 'b', 'c',
    ['d', 'e', 'f'],
    {'c': 'e', 15: '123'}
]
print(type(var_list))

# 元组 tuple
var_tuple = (1, 2, 3, 'a', 'b', 'c')
print(type(var_tuple))

# 字典 dict
var_dict = {
    'a': '123', 'b': 456,
    (1, 'a'): '123'
}
print(type(var_dict))

# 字典视图 dict_items
var_dict = {
    'a': '123', 'b': 456,
    (1, 'a'): '123'
}
print(type(var_dict.items()))

# 空 NoneType
var_none = None
print(type(var_none))
