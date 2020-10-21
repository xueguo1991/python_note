#-----------------------------------
# 内置函数 list
#-----------------------------------

# list实际上是一个类，并非内置函数, 但可以当做内置函数来用
# list会展开序列，返回数组
var_str = 'good morning.'
print(list(var_str))

var_tuple = ('good', 'morning')
print(list(var_tuple))

var_array = [100, '900', 20]
print(list(var_array))