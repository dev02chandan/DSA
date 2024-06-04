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
'''

'''
n = 4
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print('*', end='')
    for j in range(i):
        print(' ', end='')
    print()

# *****  i=0  spaces=0 => spaces = i 
#  ***   i=1  spaces=1 => stars = n-i
#   *    i=2  spaces=2
'''

'''
n = 4

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*', end='')
    for j in range(n-i-1):
        print(' ', end='')
    print()

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print('*', end='')
    for j in range(i):
        print(' ', end='')
    print()

# Mixture of the last two patterns
#    *   
#   ***  
#  ***** 
# *******
# *******
#  ***** 
#   ***  
#    *   
'''


'''
n = 4
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

#   *  
#   **
#   ***  
#   **
#   * 
'''

'''
# Method 1
# n = 5
# binary = 1
# first = 1
# for i in range(n):
#     for j in range(i+1):
#         if j == 0: 
#             print(first, ' ', end='')
#             continue
#         print(binary, ' ', end='')
#         binary = 0 if binary==1 else 1
#     print()
#     first = 0 if first==1 else 1

# Method 2 
# n = 5
# binary = 1
# for i in range(n):
#     binary = 1 if i%2==0 else 0
#     for j in range(i+1):
#         print(binary, end=' ')
#         binary= 0 if binary==1 else 1
#     print()
        

1      # j=0, i=0
0 1    # j=0,1, i=1
1 0 1  # j=0,1,2, i=2

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
'''

'''
n = 5
num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end='\t') 
        num += 1
    print()



1
2 3
4 5 6

1
2       3
4       5       6
7       8       9       10
11      12      13      14      15


'''

'''
n = 5
for i in range(n):
    for j in range(2*n):
        if j>i and j<2*n-i-1:
            print(' ', end='')
        elif j<=i:
            print(j+1, end='')
        else:
            print(2*n-j, end='')
    print()



1    1          i=0     j=0,  1,2,3,4,  5
12  21
123321

1        1
12      21
123    321
1234  4321
1234554321


'''

'''
n = 6
variable = 65
for i in range(n):
    for j in range(i+1):
        print(chr(variable), end=' ')
        variable+=1 
    print()
    variable=65



A
A B
A B C

A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
'''



'''

n = 6
var = 65
for i in range(n):
    for j in range(n-i):
        print(chr(var), end='')
        var += 1
    var = 65
    print()

A B C
A B
A
ABCDEF
ABCDE
ABCD
ABC
AB
A

'''

n = 6
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end='\t')
    print()

'''
A
B B
C C C

A
B       B
C       C       C
D       D       D       D
E       E       E       E       E
F       F       F       F       F       F
'''
