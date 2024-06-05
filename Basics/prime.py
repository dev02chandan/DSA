def isPrime(x:int):
    for i in range(2, x//2+1):
        if x%i==0:
            return False
        
    return True


def isPrime(x:int):

    '''
    We can optimise the algorithm by only iterating up to the square root of n when checking for factors. This is because if n has a factor greater than its square root, it must also have a factor smaller than its square root.
    '''

    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
        
    return True


print(isPrime(17))
print(isPrime(71))
print(isPrime(54))
print(isPrime(25))
print(isPrime(16))
print(isPrime(13))
