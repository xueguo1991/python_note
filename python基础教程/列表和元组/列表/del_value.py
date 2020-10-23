#-----------------------------------
# 内置函数删除元素
#-----------------------------------

arr = ['a', 'b', 'c', 'd', 'e', 'f']

del arr[3]

print(arr)

# 不能删除不存在的元素
# del arr[10]
# IndexError: list assignment index out of range

del arr[2:3]
print(arr)
