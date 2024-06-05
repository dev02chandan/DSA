def f(n):
    if n==0: return 
    print(n)
    n -= 1
    f(n)

f(3)