#-----------------------------------
# 类的创建及实例化
#-----------------------------------

# 类名称遵守大驼峰命名规则
class Phone :
    # 声明类属性
    obj_counter = 0
    # 声明的属性必须有默认值, 否则会变成值调用
    # NameError: name 'type_code' is not defined
    # type_code

    # 声明类方法
    def ring(self) :
        print('weng...weng......')

    # 声明隐私方法, 用两个下划线开头就表示此方法私有不可访问
    def __isActive(self):
        if self.obj_counter > 0 :
            print('已激活')
        else :
            print('未激活')

    # 类的方法声明中必须有self关键字
    # 否则报错
    # TypeError: start_up() takes 0 positional arguments but 1 was given
    # def start_up() :
    #     print('欢迎使用本手机')

# 类的实例化
my_phone = Phone()
# 调用类方法
my_phone.ring()
# 访问类属性
print(my_phone.obj_counter)
# 访问类中的隐私方法报错
# AttributeError: 'Phone' object has no attribute '__isActive'
# my_phone.__isActive()
