import time
import random

large_arr = [random.randint(1, 1000) for _ in range(100000)]
large_queries = [random.randint(1, 1000) for _ in range(1000)]

arr = [15, 2, 3, 2, 4, 5, 2, 34, 234, 234, 234, 23, 432, 234]
queries = [2, 3, 234]

def count_frequency_1(arr, queries):
    map = {}
    for i in queries:
        map[i] = 0
        for j in arr:
            if j == i:
                map[i] += 1
    return map

def count_frequency_2(arr, queries):
    map = {}
    for i in arr:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
    
    ans = {}
    for i in queries:
        if i in map.keys():
            ans[i] = map[i]
        else:
            ans[i] = 0

    return ans

# Measure time for count_frequency_1
start_time_1 = time.time()
result_1 = count_frequency_1(large_arr, large_queries)
end_time_1 = time.time()

# Measure time for count_frequency_2
start_time_2 = time.time()
result_2 = count_frequency_2(large_arr, large_queries)
end_time_2 = time.time()

print("Result from count_frequency_1:", result_1)
print("Time taken by count_frequency_1:", end_time_1 - start_time_1)

print("Result from count_frequency_2:", result_2)
print("Time taken by count_frequency_2:", end_time_2 - start_time_2)
