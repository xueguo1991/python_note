#-----------------------------------
# 格式设置微语言 值的格式化
#-----------------------------------

# b 二进制
str = '数值 {num} 的二进制表示: {num:b}'
print(str.format(num=100))

# o 八进制
str = '数值 {num} 的八进制表示: {num:o}'
print(str.format(num=100))

# d 十进制
str = '数值 {num} 的十进制表示: {num:d}'
print(str.format(num=100))

# x 十六进制
str = '数值 {num} 的十六进制表示: {num:x}'
print(str.format(num=100))

# X 十六进制 ABCDEF

# c 数字转Unicode码表所对应的字符
str = '将数值 {num} 翻译为Unicode码点: {num:c}'
print(str.format(num=97))
str = '将数值 {num} 翻译为Unicode码点: {num:c}'
print(str.format(num=98))
str = '将数值 {num} 翻译为Unicode码点: {num:c}'
print(str.format(num=99))

# e 将数值使用科学计数法表示
str = '数值 {num} 的科学法表示表示(用e表示指数): {num:e}'
print(str.format(num=100.512))
str = '数值 {num} 的科学法表示表示(用大写E表示指数): {num:E}'
print(str.format(num=100.512))

# f 浮点数 nan和inf都小写
str = '数值 {num} 表示为浮点数: {num:.3f}'
print(str.format(num = 3.14159265534343))
str = '数值 {num} 不存在时 {num:.3f}'
print(str.format(num = float('nan')))
str = '数值 {num} 不存在时 {num:.3f}'
print(str.format(num = float('inf')))

# F 浮点数 NAN和INF都大写
str = '数值 {num} 表示为浮点数: {num:.3F}'
print(str.format(num = 3.14159265534343))
str = '数值 {num} 不存在时 {num:.3F}'
print(str.format(num = float('nan')))
str = '数值 {num} 不存在时 {num:.3F}'
print(str.format(num = float('inf')))

# % 百分比 按照 f 的方式设置百分比数值
str = '数值 {num} 的百分比表示为: {num:.2%}'
print(str.format(num=0.547983432))
