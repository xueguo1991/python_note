#-----------------------------------
# pass 关键字
#-----------------------------------
import random

num = random.randint(1, 100)

if 1 <= num < 30 :
    print('{}介于前三分之一'.format(num))
elif 30 <= num < 60 :
    # 待处理
    pass
else :
    print('{}大于等于60')