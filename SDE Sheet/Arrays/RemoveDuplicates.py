def removeDuplicates(arr, n):
    count = 0
    for i in range(n):
        if i != 0 and arr[i] == arr[i-1]:
            continue
        count += 1

    return count

# Two Pointer Approach where j finds the next unique element
# Both solutions are optimal
# TC = O(N)
# SC = O(1)

# Brute : Use a set O(N)
