arr = ['a', 'b', 'c', 'd', 'e', 'f']

# 使用切片可以批量给列表赋值
arr[0:3] = 'kkk'
print(arr)
arr[0:3] = ['0', '0', '0']
print(arr)

# 使用切片这样赋值实现向列表头部添加元素的功能
arr[0:0] = ['a', 'b', 'c']
print(arr)
# 使用切片这样赋值实现向列表尾部追加元素的功能
arr[len(arr):len(arr)] = ['s', 's', 's']
print(arr)

# 切片赋值必须是序列
# ！！arr[2:5] = 5
# TypeError: can only assign an iterable
