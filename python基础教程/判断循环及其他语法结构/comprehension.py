#-----------------------------------
# 列表推导 及 字典推导
#-----------------------------------

# 简单推导
x = [ 2 * i for i in range(103, 109)]
print(x)

print()

# 推导嵌套
x = [(x, y) for x in range(3) for y in range(3)]
print(x)

print()

# 带有条件的推导
x = [x for x in range(100) if x % 29 == 0]

# 字典推导
a = {'师傅': '唐僧', '大徒弟': '悟空', '二徒弟': '八戒'}
x = {a[x] for x in a}
y = {x for x in a}
z = {'{}是{}'.format(a[x], x) for x in a}
w = {'[' + x + ']': '>' + a[x] + '<' for x in a}
print(x)
print(y)
print(z)
print(w)