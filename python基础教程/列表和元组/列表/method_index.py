#-----------------------------------
# 列表方法 查找元素第一次出现的索引
#-----------------------------------

arr = ['a', 'b', 'c', 'a', 'b', 'c']
print(arr.index('c'))
print(arr.index('a'))
#  查找不存在的元素将引发异常
# print(arr.index('d'))
# ValueError: 'd' is not in list