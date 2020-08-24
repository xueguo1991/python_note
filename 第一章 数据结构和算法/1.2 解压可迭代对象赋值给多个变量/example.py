arr = ['王某', '男', 1, 2, 4, 56, 78]
# 一次性将多个可迭代元素赋值给一个变量
# 注意此处 * 号写在变量的前方
var_name, var_sex, *_ = arr
print(var_name, var_sex)

# 这种写法专门为不确定元素个数的赋值过程而设计
var_first, *var_not_sure, var_last = ['first', 1, 2, 3, 4, 4, 5, 6, 7, 7, 'last']
print(var_first, var_last)


# _也是一个变量，只不过是个普通的变量，用来承载不需要再被使用的数据
print(_)
