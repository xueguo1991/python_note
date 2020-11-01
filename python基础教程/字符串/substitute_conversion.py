#-----------------------------------
# 格式设置微语言 转换标识
# ! 开头， 将数据转换成不同的字符串呈现形式
#-----------------------------------

# 转换表示有三种
# r representation 将数据转换为python表示的形式
# s string 将数据转换为字符串表示形式
# a ascii 将数据转换为ASCII码表示形式


# ------  r 转换标识  --------------

str = '字符串的python表示：{!r}'
print(str.format('我是一行字符串'))

str = '数组的python表示：{!r}'
print(str.format(['a', 'b', 'c']))

str = '元组的python表示：{!r}'
print(str.format((2,3)))

# ------  s 转换标识  --------------

str = '普通的字符串表示: {!s}'
print(str.format('我是一行字符串'))

str = '将浮点数转为字符串表示: {!s}'
print(str.format(12.87343))

str = '将元组转为字符串表示: {!s}'
print(str.format((1, 2, 3)))

# ------  a 转换标识  --------------
str = '汉字的ASCII码表示: {!a}'
print(str.format('我是一行字符串'))

str = '数组的ASCII码表示: {!a}'
print(str.format([1, 2, 3]))

str = '元组的ASCII码表示: {!a}'
print(str.format(('a', 'b', 'c')))