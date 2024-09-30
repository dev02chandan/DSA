import math

def isArmstrong(x):
    length = int(math.log10(x) + 1)

    if length < 2: 
        return True
    num = x
    sum = 0
    for i in range(length):
        sum += (num%10)**length
        num = num // 10

    if sum == x:
        return True
    
    else:
        return False


    


print(isArmstrong(153))
print(isArmstrong(213))
print(isArmstrong(371))
print(isArmstrong(9))
print(isArmstrong(23))