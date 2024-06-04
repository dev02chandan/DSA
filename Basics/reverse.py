num = 1234
# print(int(str(num)[::-1]))

revNum = 0
i = 0
while(True):
    temp = num%10
    revNum = revNum*(10)
    # revNum += revNum*(10**i) + num%10
    revNum += temp
    num = num//10
    i+=1
    if num ==0:
        break

print(revNum)

