#-----------------------------------
# 列表方法 列表排序
#-----------------------------------

arr = ['a', 'b', 'c', 'd', 'e', 'f']
arr.sort()
print(arr)

arr = ['a', 'b', 'c', 1, 500, 30, 200, 3]
# arr.sort()
# 排序时不能对多种数据类型的序列排序
# TypeError: '<' not supported between instances of 'int' and 'str'
# print(arr)

arr = ['a', 'b', 'c', 'abc', 'ab1', 'ab', '1', '2', '3','100', '10']
arr.sort()
# 对字符串排序时是字典序
print(arr)

arr = ['a', 'b', 'c', 'abc', 'ab1', 'ab']
arr_sorted = sorted(arr)
# 对序列排序
print(arr)
print(arr_sorted)

arr = ['abc','ab', 'xy', '1', '666zz', 'zzz', 'i中国', '世界']
arr.sort(key=len)
# 使用关键字参数 len 指定按照长度排列
print(arr)

arr = ['abc','ab', 'xy', '1', '333']
arr.sort(reverse=True)
# 字典序倒叙排列
print(arr)

arr = ['abc','ab', 'xy', '1', '333']
arr.sort(reverse=False)
# 字典序正序排列
print(arr)
