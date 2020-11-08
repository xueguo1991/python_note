#-----------------------------------
# 类的继承
#-----------------------------------

class Phone :
    system = ''
    def ring(self) :
        print('weng...weng...')
    def screen(self) :
        print('触摸屏')

# 单继承
# 在子类中要指明继承自超类的名称, 使用圆括号把类名括起来
class Huawei (Phone):
    system = 'huawei'
    def screen(self) :
        print('京东方触摸屏')

class Camera (Phone) :
    def photo(self):
        print('日本卡尔蔡司镜头')
    def screen(self) :
        print('三星代工')

class Car :
    pass

# 多重继承
# 多继承的类方法重复定义时, 按照下面括号内的继承先后顺序, 先继承的方法会覆盖掉后面所有的同名方法
# 继承循序算法很复杂, 最好少用多重继承
# TypeError: Cannot create a consistent method resolution
class Hornor (Camera, Huawei, Phone) :
    pass

my_phone = Huawei()
print(my_phone.system)
my_phone.ring()
my_phone.screen()

print()

bob_phone = Hornor()
bob_phone.screen()
bob_phone.photo()
