arr = [0,2,34,23,356,123,23,123,123,213,123,312,123,243,423,345,435,65,756,746,534,423]

def find_highest_and_lowest_freq(arr):
    map = {}
    for i in arr:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
    
    
    # Traversing again - can be improved by checking in the same loop
    
    max_key = max(map, key = map.get)
    min_key = min(map, key= map.get)

    return max_key, min_key


print(find_highest_and_lowest_freq(arr))




