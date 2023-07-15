def solveNQueens(n):

    # Matrix is a list of strings
    matrix = ["0"*n for _ in range(n)]
    ans = []

    def Check(row, col):

        duplrow = row
        duplcol = col

        # check upward
        while (col >= 0):
            if matrix[row][col] == '1':
                return False
            col -= 1

        col = duplcol

        # Check diagonally left up
        while (col >= 0 and row >= 0):
            if matrix[row][col] == '1':
                return False
            row -= 1
            col -= 1

        col = duplcol
        row = duplrow

        # Check Diagonally left down
        while (col >= 0 and row < n):
            if matrix[row][col] == '1':
                return False
            col -= 1
            row += 1

        return True

    def solver(col):

        if col == n:
            ans.append(' '.join(list(matrix)))
            return

        for row in range(n):
            if Check(row, col):

                matrix[row] = matrix[row][:col] + '1' + matrix[row][col+1:]

                solver(col + 1)

                matrix[row] = matrix[row][:col] + '0' + matrix[row][col+1:]

    solver(0)

    return ans
