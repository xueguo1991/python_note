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