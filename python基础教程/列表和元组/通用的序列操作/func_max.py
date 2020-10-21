#-----------------------------------
# 内置函数 max()
#-----------------------------------

# 最大值
var_str = '129111'
print(max(var_str))
# 最大值类型var_array = ['15', 9, 1]
# TypeError: '>' not supported between instances of 'int' and 'str'
# !! 注意这里，序列中元素是字符串时，相当于序列嵌套序列
# 所以下面的变量最大值是 8
var_array = ['15', '8', '1']
print(max(var_array))
var_tuple = (1, 15, 999)
print(max(var_tuple))