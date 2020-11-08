#-----------------------------------
# 闭包
#-----------------------------------

def getY(x):
    y = x ** 2
    print('x = {} y = {}'.format(x, y))

    def carrier(c):
        print('c = {} y = {}'.format(c, y))
        return y * c
    return carrier

func_y = getY(100)
func_y(12)

print()

# 作用域嵌套发生的变量覆盖问题

def a() :
    num = 20
    print('我是函数a, num={}'.format(num))

    def b() :
        num = 30
        print('我是函数b, num={}'.format(num))

    print('函数a中的 num={}'.format(num))
    def c() :
        # 这里使用nonlocal关键字生命, 这里使用的num是闭包函数c之外的变量
        nonlocal num
        num = 40
        print('我是函数c, num={}'.format(num))

    b()
    c()
    print('函数a中的 num={}'.format(num))

num = 100
a()
print('最外部的num = {}'.format(num))
