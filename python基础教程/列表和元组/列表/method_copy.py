#-----------------------------------
# 列表方法 复制列表
#-----------------------------------

arr = ['a', 'b', 'c']

arr_fake = arr
arr_fake[0] = 'aaa'
# 普通变量赋值的方法是传递变量指针，新列表的修改会影响旧列表
print(arr)


arr = ['a', 'b', 'c']
arr_fake = arr.copy()
arr_fake[0] = 'aaa'
# copy方法会将原变量复制一份
print(arr)


arr = ['a', 'b', 'c']
arr_fake = arr[:]
arr_fake[0] = 'aaa'
# 切片会复制原变量，完整切片效果等同于copy
print(arr)

arr = ['a', 'b', 'c']
arr_fake = list(arr)
arr_fake[0] = 'aaa'
# list 函数会复制原变量， 效果等同于copy
print(arr)