#-----------------------------------
# 异常的顺序
#-----------------------------------


def exception_1() :
    raise Exception('这里发生了火灾')

def ignore_exception() :
    print('这里发生的一切都将被忽略')
    exception_1()

def main_func() :
    print('我是主程序')
    try:
        ignore_exception()
    except Exception as e:
        print(e)

main_func()