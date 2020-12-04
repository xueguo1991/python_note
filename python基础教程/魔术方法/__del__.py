#-----------------------------------
# 析构函数
#-----------------------------------

class Robot() :
    def say(self) :
        print('I am robot, what do you need')

    def __del__(self):
        print('I am dead, leave me in peace')

robot = Robot()
robot.say()

del robot
