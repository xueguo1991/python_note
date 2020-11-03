#-----------------------------------
# if 条件句
#-----------------------------------
import random

num = random.randint(1, 3000)

if num < 1000 :
    print('{}小于1千'.format(num))
elif num >= 1000 and num < 2000 :
    print('{}大于等于1千且小于2千'.format(num))
    print()
    if num >= 1000 and num <= 1500 :
        print('{}大于等于1千且小于等于1千5'.format(num))
    else :
        print('{}大于1千5且小于2千')
else :
    print('{}大于等于2千'.format(num))
