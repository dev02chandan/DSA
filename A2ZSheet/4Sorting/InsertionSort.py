arr = [2, 8, 5, 3, 9, 4]

def insertionSort(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            j = i
            while(arr[j-1] > arr[j]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j-=1
                if j == 0:
                    break
        print(arr)
insertionSort(arr)