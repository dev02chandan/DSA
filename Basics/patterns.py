'''
n = 5
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()

*****
*****
*****
*****
*****
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if j<=i:
            print('*', end='')
    print()

*
**
***
****
*****
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if j<=i:
            print(j+1, end='')
    print()


1
12
123
1234
12345
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if j<=i:
            print(i+1, end='')
    print()

1
22
333
4444
55555
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if n-i > j:
            print("*", end='')
    print()


# 0, 1, 2, 3, 4 (i)
# 0, 1, 2, 3, 4 (j)

# 5 - 0 > 0, 1, 2, 3, 4
# 5 - 1 > 0, 1, 2, 3

*****
****
***
**
*
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if n-i > j:
            print(j+1, end='')
    print()
12345
1234
123
12
1
'''

n = 3
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*', end='')
    for j in range(n-i-1):
        print(' ', end='')
    print()


#     *      i=0 4 spaces => 5-0-1 spaces
#    ***     i=1 3 spaces => 5-1-1 spaces
#   *****    i=2 2 spaces => ...
#  *******   i=3 1 spaces
# *********  i=4 0 spaces => n-i-1 spaces


