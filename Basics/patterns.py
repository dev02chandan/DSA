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
n = 9
var = n//2
for i in range(var+1):
    for j in range(n):
        if j<var or j>=(n-var):
            print(" ", end="")
        else:
            print("*", end='')
    print()
    var-=1

# 0,1,2,3,4,5,6,7,8
# var = 4
# var = 3

    *    
   ***   
  *****  
 ******* 
*********

'''

# n = 9
# var = n//2
# for i in range(var+1):
#     for j in range(n):
#         if :
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()
#     var-=1

# 0, 1, 2, 3, 4 (i)
# 0, 1, 2, 3, 4, 5, 6, 7, 8 (j)



