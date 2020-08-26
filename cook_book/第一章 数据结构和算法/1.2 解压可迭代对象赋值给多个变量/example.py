arr = ['王某', '男', 1, 2, 4, 56, 78]
# 一次性将多个可迭代元素赋值给一个变量， PHP没有这样的功能
# 注意此处 * 号写在变量的前方
var_name, var_sex, *_ = arr
print(var_name, var_sex)

# 这种写法专门为不确定元素个数的赋值过程而设计
var_first, *var_not_sure, var_last = ['first', 1, 2, 3, 4, 4, 5, 6, 7, 7, 'last']
print(var_first, var_last)
# 中间不确定的变量一定会集合到一个序列中, 哪怕只有1个元素，或0个元素
print(var_not_sure)
var_first, *var_not_sure, var_last = ['first', 1, 'last']
print(var_not_sure)
var_first, *var_not_sure, var_last = ['first','last']
print(var_not_sure)

# 不允许使用两个不确定变量, 因为这在逻辑上也讲不通
# 否则会报错： SyntaxError: two starred expressions in assignment
# var_first, *var_not_sure, *var_not_sure, var_last = ['first', 1, 2, 3, 4, 4, 5, 6, 7, 7, 'last']



# _也是一个变量，只不过是个普通的变量，用来承载不需要再被使用的数据
print(_)

# 特别是用在迭代中，这样的赋值会让开发有神来之笔的效率

var_grades = [
    ['numbers', 12.5, 14, 15],
    ['levels', '甲'],
    ['numbers', 45, 13, 20],
    ['numbers', 34, 12, 9],
    ['levels', '乙']
]

for grade_type, *grades in var_grades:
    if grade_type == 'numbers':
        tmp_sum = sum(grades)
        tmp_len = len(grades)
        tmp_len = 1 if tmp_len == 0 else tmp_len
        print('平均分成绩：{avg:.2f}'. format(avg = tmp_sum / tmp_len))

    if grade_type == 'levels':
        print('分级成绩：{level}'.format(level = grades[0]))

# *号和变量名之间不是必须紧挨着的， * 号是一种运算符
var_a, *  var_b, var_c = [1, 1, 1, 1, 1, 1]
print(var_a, var_b, var_c)