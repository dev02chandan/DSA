def rotate(matrix: list[list[int]]) -> None:
    # first transpose of the matrix and then reverse each row
    # the diagonals remain the same and the indices are swapped for a transpose

    for i in range(len(matrix)):
        for j in range(len(matrix)-1, i, -1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix)//2):
            matrix[i][j], matrix[i][len(
                matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
