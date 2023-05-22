matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix)-1, i, -1):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
