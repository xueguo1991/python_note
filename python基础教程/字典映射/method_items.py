#-----------------------------------
# 字典方法 字典列表
#-----------------------------------

x = {'师傅': '唐僧', '二徒弟': '八戒', '行李': ['袈裟', '禅杖']}
print(x.items())
print(type(x.items()))
x_items = x.items()

x['师傅'] = '唐三藏'
# 字典视图始终是字典的一种反应， 并非副本， 可查不可改
print(x_items)
print(len(x_items))
print(('师傅', '唐三藏') in x_items)

# 字典视图不可修改
# x_items['师傅'] = '唐御弟'
# TypeError: 'dict_items' object does not support item assignment


# 字典视图虽然不可修改， 但是不能作为字典的键
# TypeError: unhashable type: 'dict_items'
# y = {x_items: '112312'}
