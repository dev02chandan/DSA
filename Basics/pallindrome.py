num = 10340
num2 = 12321

def reversed(num):
    revNum = 0
    while True:
        revNum = revNum*10 + num%10
        num = num//10
        if num==0:
            break   
    return revNum

def isPall(num):
    return reversed(num) == num

print(isPall(num))
print(isPall(num2))

# TC O(log_10(N) + 1)
# SC O(1)