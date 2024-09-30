num = -12340
# print(int(str(num)[::-1]))

def reversed(num):
    revNum = 0
    while True:
        revNum = revNum*10 + num%10
        num = num//10
        if num==0:
            break   
    return revNum

print(reversed(num))



# Leet code

'''
class Solution:
    def reverse(self, x: int) -> int:
        revNum = 0
        num = abs(x)

        while True:
            revNum = revNum * 10 + num % 10
            num = num//10
            if num == 0:
                break

        if revNum > 2**31 or revNum < 2**(-31):
            return 0

        if x < 0: 
            return -(revNum)
        else:
            return revNum

'''