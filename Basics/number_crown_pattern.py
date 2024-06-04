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


'''
1    1          i=0     j=0,  1,2,3,4,  5
12  21
123321

1        1
12      21
123    321
1234  4321
1234554321
'''