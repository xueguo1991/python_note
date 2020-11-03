#-----------------------------------
# for 循环
#-----------------------------------

# 常规列表循环
for i in range(10):
    print(i)

print()

# 字典循环
x = {'师傅': '唐僧', '二徒弟': '八戒', '大徒弟': '悟空'}
for key in x :
    print(key, x[key])

print()

# continue跳过
# break中断
for i in range(0, 100, 3) :

    if i == 9 : continue
    if i == 15 : break

    print(i)

print()

# for else 结构, python特有,
# 当for循环顺利执行完时,执行else部分
# 但如果没有顺利执行完, 中途break, else 部分不执行

for i in range(1, 3) :
    print('当前数字:{}'.format(i))

else :
    print('循环完成')

print()

for i in range(1, 3) :
    print(i)
    if i == 2 : break
else :
    print('循环完成')