#-----------------------------------
# 字典方法 清空
#-----------------------------------

dictionary = {'大徒弟': '悟空', '师傅': '唐僧'}
dictionary.clear()
# 清空字典
print(dictionary)

# 场景一
x = {}
y = x
x['master'] = '唐僧'
print(y)
# 如下方式清空x的值时， 不会影响到y
x = {}
print(y)

# 场景二
x = {}
y = x
x['master'] = '唐僧'
print(y)
# 如下方式清空x的值时， y同时被清空
x.clear()
print(y)