import time


n1 = 432342222
n2 = 1223433333


def GCD1(n1, n2):
    start_time = time.time()
    gcd = 1 
    for i in range(1, min(n1, n2) + 1):  
        if n1 % i == 0 and n2 % i == 0:
            gcd = i  
    end_time = time.time()
    print(f"GCD2: {gcd} ({end_time - start_time:.6f} seconds)")
    return gcd


def GCD2(n1, n2):
    start_time = time.time()
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
            break
    end_time = time.time()
    print(f"GCD2: {gcd} ({end_time - start_time:.6f} seconds)")

def GCD3(n1, n2):
    '''
    The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers.
    It operates on the principle that the GCD of two numbers 
    remains the same even if the smaller number is subtracted from the larger number.
    '''
    start_time = time.time()

    if n1 == 0:
        end_time = time.time()
        print(f"GCD3: {n2} ({end_time - start_time:.6f} seconds)")
        return n2
    if n2 == 0:
        end_time = time.time()
        print(f"GCD3: {n1} ({end_time - start_time:.6f} seconds)")
        return n1
    
    newNum = max(n1, n2) - min(n1, n2)
    GCD3(newNum, min(n1, n2))

GCD1(n1, n2)
GCD2(n1, n2)
GCD3(n1, n2)

'''
Example time: 
GCD2: 3 (22.476354 seconds)
GCD2: 3 (21.272650 seconds)
GCD3: 3 (0.000001 seconds)
'''