#-----------------------------------
# 序列的加法运算
#-----------------------------------

# 两个数组序列可以自由相加合并，被加的序列按照加的顺序往后排
arr_a = ['a', 'b', 'c']
arr_b = [1, 2, 3]
print(arr_a + arr_b)
# 序列不能相减
# print(arr_a - arr_b)

# 字符串序列相加实现了字符串的拼接
str_a = 'world'
str_b = ' hi'
print(str_a + str_b)


# 虽然字符串和数组都是序列， 但是不同类型的序列不能相加
# print(arr_a + str_b)
# TypeError: can only concatenate list (not "str") to list