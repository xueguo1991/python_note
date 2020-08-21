# python严格区分了数组和字典，它们有不同的表示方式
# PHP 关联数组 ['aa' => 'bb'] 在python中不允许的

# 数组元素可以是不同的数据类型，这点和PHP相同
arr = [1, 'a', ['a', 'b', 'c'], 1.2, True]

# 将序列分解为单独的变量，左边变量数必须等于序列中的元素个数
# 序列中元素的数据类型是什么，都可以这样被赋值
# PHP中相同的功能需要通过list()函数来实现： list($a, $b) = [111, 'aaa']
var_int, var_string, var_arr, var_float, var_bool = arr
print([var_int, var_string, var_arr, var_float, var_bool])

# 空白占位符可以在这种方式创建变量时抛弃序列中不需要的元素
_, _, _, var_last = [1, 2, 4, 'I am last']
print(var_last)
