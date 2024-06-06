
n = 5 # 0 based indexing

def fib(n):
    term1 = 0
    term2 = 1
    print(term1)
    print(term2)
    for i in range(n-1):
        print(term1 + term2)
        if term1 < term2:
            term1 = term1 + term2
        else:
            term2 = term1 + term2
    

def fib(n):
    '''
    In this approach, instead of printing the Fibonacci series till N,
    we’re going to print the Nth Fibonacci number using functional recursion with multiple function calls.
    '''
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

print(fib(n))

# Time Complexity: O(2^N) 
# Space Complexity: O(N)