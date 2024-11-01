import math

def second_largest_smallest(arr, n):
    large1 = -math.inf
    large2 = -math.inf
    small1 = math.inf
    small2 = math.inf

    for i in range(n):
        if arr[i] > large1:
            large2 = large1
            large1 = arr[i]
        elif arr[i] > large2:
            large2 = arr[i]
        
        if arr[i] < small1:
            small2 = small1
            small1 = arr[i]
        elif arr[i] < small2:
            small2 = arr[i]
    
    if large2 == -math.inf:
        large2 = arr[-2]
    if small2 == math.inf:
        small2 = arr[-2]

    return [large2, small2]


arr = [1,2,3,4,5]
print(second_largest_smallest(arr, len(arr)))

arr = [5,4,3,2,1]
print(second_largest_smallest(arr, len(arr)))

arr = [3, 4, 5, 2]
print(second_largest_smallest(arr, len(arr)))