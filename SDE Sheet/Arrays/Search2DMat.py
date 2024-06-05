def searchMatrix(mat, target: int) -> bool:
    # Using Imaginary Indices
    # Row = Imaginary // 2
    # Col = Imaginary % 2

    # Set the low and high indices for binary search
    low = 0
    high = len(mat) * len(mat[0]) - 1

    # Perform binary search until low <= high
    while low <= high:
        # Calculate the middle index
        mid = low + (high - low) // 2

        # Retrieve the element at the corresponding row and column
        element = mat[mid // len(mat[0])][mid % len(mat[0])]

        # If the target is found, return True
        if element == target:
            return True

        # If the element is less than the target, move the low index to the right
        elif element < target:
            low = mid + 1

        # If the element is greater than the target, move the high index to the left
        else:
            high = mid - 1

    # If the target is not found, return False
    return False
# Test Cases


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 2))
