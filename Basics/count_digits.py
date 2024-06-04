import time, math
start_time = time.time()

# Brute force approach is to do % 10 and count every time 
# optimal is O(1) by log or str 
n = 12345
# print(len(str(n)))
print(int(math.log10(n) + 1))


print("--- %s seconds ---" % (time.time() - start_time))

