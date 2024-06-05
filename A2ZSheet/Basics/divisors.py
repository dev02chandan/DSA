def printDivisors(x: int):
    ans = []
    for i in range(1, x//2+1):
        if x % i == 0:
            ans.append(i)
    ans.append(x)
    return ans


def printDivisors(x: int):
    '''
    We can optimise the previous approach by using the property that for any non-negative integer n,
    if d is a divisor of n then n/d is also a divisor of n.
    '''
    ans = []
    for i in range(1, int(x**0.5)+1):    
        if x % i == 0:
            ans.append(i)
            if i != x//i:
                ans.append(x//i)
    return ans

print(printDivisors(36))
print(printDivisors(45))
print(printDivisors(108))
print(printDivisors(12))

# Time Complexity: O(sqrt(N))
# Space Complexity : O(2*sqrt(N))