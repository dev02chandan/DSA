num = 12340
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

