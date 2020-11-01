#-----------------------------------
# 格式设置微语言 字段名的替换
#-----------------------------------

str = '{}骑着马，{}挑着担, {}在飞, {}在偷懒'
# 顺序替换， 占位符数目必须必须小于format中的参数个数相同
# 否则报错：IndexError: tuple index out of range
print(str.format('唐僧', '沙僧', '悟空', '八戒'))

str = '{2}骑着马，{3}挑着担, {0}在飞, {1}在偷懒, {1}啊{1}'
# 索引替换 索引数目必须小于format参数个数
# 索引超过范围：
# IndexError: tuple index out of range
# 使用索引替换， 要保证format中的参数顺序不能乱， 占位符则随意安排
print(str.format('悟空', '八戒', '唐僧', '沙僧'))

str = '{ts}骑着马，{ss}挑着担, {wk}在飞, {bj}在偷懒, {bj}啊{bj}'
# 字段名替换 字段名必须在format中声明
# 未找到对应的字段名：
# SyntaxError: positional argument follows keyword argument
# 使用字段名替换， 对参数顺序无要求， 最为灵活
print(str.format(wk = '悟空', ts = '唐僧', bj = '八戒', ss = '沙僧'))

# str = '{}骑着马，{}挑着担, {0}在飞, {1}在偷懒, {1}啊{1}'
# 索引替换与顺序替换不能混用:
# ValueError: cannot switch from automatic field numbering to manual field specification
# 这样会导致代码混乱不堪
# print(str.format('悟空', '八戒', '唐僧', '沙僧'))

str = '{0}骑着马，{1}挑着担, {wk}在飞, {bj}在偷懒, {bj}啊{bj}'
# 索引替换与字段名替换可以混用， 但不推荐
# 混用时， format中， 索引字段必须排在前， 且个数大于索引
print(str.format('唐僧', '沙僧', wk = '悟空',  bj = '八戒',))

str = '{}骑着马，{}挑着担, {wk}在飞, {bj}在偷懒, {bj}啊{bj}'
# 顺序替换与字段名替换可以混用， 但不推荐
# 混用时， format中， 顺序字段必须排在前， 且个数大于占位数
print(str.format('唐僧', '沙僧', wk = '悟空',  bj = '八戒',))
