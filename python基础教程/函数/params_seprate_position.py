#-----------------------------------
# 传递参数 分配位置参数
#-----------------------------------

x = ('孙行者', '行者孙', '者行孙')

# 分配位置参数的关键参数:
# 分配位置参数时, 实参列表与形参个数要相等
def separate(x, y, z):
    print(x, y, z)

separate(*x)