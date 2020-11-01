#-----------------------------------
# 字符串格式设置 使用format方法
#-----------------------------------

#------- 基本使用 ---------
# 使用 {} 占位替换文字
str = '我的编号是{} 我的营业额是{}'
print(str.format('00100',  15.88))

# 使用索引决定替换顺序
str = '唐僧师徒四人分别是 {2}, {1}, {3}, {0}'
print(str.format('猪八戒', '唐僧', '悟空', '沙僧'))

# 使用关键字参数
str = '我的编号是{no} 我的营业额是{money}'
print(str.format(no = '00100', money = 100.88))

#---------- 微型格式指定语言 ----------

# 花括号为界定符， 在最终结果中保留花括号要使用双花括号
str = '我就是大闹天宫的{{ {} }}'
print(str.format('至尊宝'))

# 字符串替换格式由三部分组成
# { [field_name] ![conversion] :[format_spec] }
# field_name 字段名， 指定替换的关键字
# conversion 数据类型转换说明符号， 感叹号开头表示要将值转换说明 !
# format_spec 格式指定， 冒号开头代表格式指定语法
# 数据类型转换符和格式指定符不能混用
