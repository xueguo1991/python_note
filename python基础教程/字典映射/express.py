#-----------------------------------
# 字典的声明
#-----------------------------------

dictionary = {'师傅': '唐僧', '大徒弟': '孙悟空'}
# 声明字典使用花括号， 键值对使用冒号连接， 键值对使用逗号分隔
print(dictionary)

dictionary = {}
# 声明空字典
print(dictionary)

dictionary = {(1, 2, 3): ['a', 'b', 'c']}
# 字典的键为元组
print(dictionary)

dictionary = {15: ('a', 'b', 'c')}
# 字典的键为数字
print(dictionary)

dictionary = {True: '真', False: '假'}
print(dictionary)
# 字典的键为布尔值

# dictionary = {[1,2,3]: ['a', 'b', 'c']}
# 字典的键必须是不可修改的数据类型， 所以不可以用列表作为键
# TypeError: unhashable type: 'list'

dictionary = {}
dictionary['大徒弟'] = '孙悟空'
# 追加元素
print(dictionary)

# 取值
print(dictionary['大徒弟'])

# 查询键
print('大徒弟' in dictionary)
print('大师兄' in dictionary)

# 字典长度
print(len(dictionary))

# 删除元素
del dictionary['大徒弟']
print(dictionary)