#-----------------------------------
# 抽象类
#-----------------------------------

from abc import ABC, abstractmethod

# 这里类Phone继承自ABC类, ABC类是一个系统抽象类, 凡是继承自
# 它的类都是抽象类
class Phone(ABC) :
    # 这里指明这个call方法是个
    @abstractmethod
    def call() :
        pass


class Hornor(ABC):
    def call(self) :
        print('华为荣耀, 你指的拥有')

my_hornor = Hornor()

my_hornor.call()