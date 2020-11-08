#-----------------------------------
# 类的私有化
#-----------------------------------

class Phone :
    # 声明私有属性
    __obj_counter = 0

    def get(self):
        self.__obj_counter += 1
        print('我可以访问隐私属性__obj_counter, 她的值是:{}'.format(self.__obj_counter))
        self.__isActive()

    # 声明私有方法, 用两个下划线开头就表示此方法私有不可访问
    def __isActive(self):
        if self.__obj_counter > 0 :
            print('已激活')
        else :
            print('未激活')
my_phone = Phone()

# 访问类中的隐私方法或隐私属性都会报错
# AttributeError: 'Phone' object has no attribute '__isActive'
# my_phone.__isActive()

# 强制访问类属性
# 强制访问时, 类属性和方法都是实例化之前的默认值
print(my_phone._Phone__obj_counter)
# 强制访问类方法
my_phone._Phone__isActive()
