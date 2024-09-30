def selection_sort(arr):
    cur_min = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j
        arr[cur_min], arr[i] = arr[i], arr[cur_min]
        print(arr)
    return arr


arr = [2, 3, 4, 5, 6, 1]
print(arr)
ans = selection_sort(arr)
print("answer ", ans)
