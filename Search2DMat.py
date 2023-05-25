def searchRow(arr, low, high, target):

    while (low <= high):

        mid = low + (high - low)//2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return False


def searchMatrix(mat, target: int) -> bool:
    i = 0
    j = len(mat[0])-1
    while (True):
        if i == len(mat):
            return False
        if mat[i][j] == target:
            return True
        elif mat[i][j] > target:
            return searchRow(arr=mat[i], low=0, high=j, target=target)
        else:
            i += 1


print(searchMatrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]], 8)
      )
