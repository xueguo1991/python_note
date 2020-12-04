#-----------------------------------
# try except 语句
# 添加大量的if else语句会降低代码可读性
#
#-----------------------------------

a = 12
b = 23

c = a + b

try :
    d = '123'
    d / 3
except ZeroDivisionError :
    print('不能除以0')
except TypeError :
    print('类型不正确')
finally:
    del c
    print('清理一些变量')