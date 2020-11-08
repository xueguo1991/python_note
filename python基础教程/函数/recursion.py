
#-----------------------------------
# 递归
#-----------------------------------

def fibs(n):
    if n > 1  :
        return fibs(n - 1) + fibs(n - 2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else :
        return 0

print(fibs(20))
