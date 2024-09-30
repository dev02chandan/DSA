def sum_of_n_numbers(n):
    return n*(n+1)/2

def sum_of_n_numbers1(n):
    '''
    sumOfNaturalNumbers(N) = N + sumOfNaturalNumbers(N-1);
    '''
    if n==0:
        return 0

    return n + sum_of_n_numbers1(n-1)

print(sum_of_n_numbers1(4))

