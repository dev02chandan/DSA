array = [1, 2, 3, 4]

def reverse(array, n):
    return array[::-1]

def reverse(array, n):
    array.reverse()
    return array

# Brute force - use an extra array O(n), O(n) (not written)

def reverse(array, n):
    for i in range(n//2):
        array[i] , array[n-i-1] = array[n-i-1], array[i]
    return array

# Remove the extra space - iterative or recursive

def reverse(array, n):
    if n < 2:
        return array

    return [array[n-1]] + reverse(array[1:n-1], n-2) + [array[0]]
    
print(reverse(array, len(array)))

