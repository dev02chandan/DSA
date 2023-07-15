def solveNQueens(n):
    # Initialize the chessboard matrix with '0'
    matrix = ["0" * n for _ in range(n)]
    ans = []  # Store the valid configurations
    leftRow = [0] * n  # Track the availability of rows
    # Track the availability of lower diagonals
    lowerDiagonal = [0] * (2 * n - 1)
    # Track the availability of upper diagonals
    upperDiagonal = [0] * (2 * n - 1)

    def solver(col):
        if col == n:
            # Add the current configuration to the result
            ans.append(' '.join(list(matrix)))
            return

        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[col + row] == 0 and upperDiagonal[col - row + n - 1] == 0:
                # Place the queen in the current position
                matrix[row] = matrix[row][:col] + '1' + matrix[row][col + 1:]
                leftRow[row] = 1  # Mark the row as occupied
                # Mark the lower diagonal as occupied
                lowerDiagonal[col + row] = 1
                # Mark the upper diagonal as occupied
                upperDiagonal[col - row + n - 1] = 1
                solver(col + 1)  # Move to the next column
                matrix[row] = matrix[row][:col] + '0' + \
                    matrix[row][col + 1:]  # Undo the changes made
                leftRow[row] = 0  # Mark the row as available again
                # Mark the lower diagonal as available again
                lowerDiagonal[col + row] = 0
                # Mark the upper diagonal as available again
                upperDiagonal[col - row + n - 1] = 0

    solver(0)  # Start the recursive solver from the first column
    return ans


# Test Case
print(solveNQueens(4))
# Expected output: ['0 0 1 0', '1 0 0 0', '0 0 0 1', '0 1 0 0',
#                   '0 1 0 0', '0 0 0 1', '1 0 0 0', '0 0 1 0']

# Approach:
# - The function uses a recursive backtracking approach to solve the N-Queens problem.
# - It represents the chessboard as a matrix of '0' and '1', where '1' represents the position of a queen.
# - The function maintains three arrays: `leftRow`, `lowerDiagonal`, and `upperDiagonal`, to keep track of the availability of rows and diagonals.
# - The recursive function, `solver`, takes a column as input and tries to place a queen in each row of that column.
# - It checks if the current row is available, along with its lower and upper diagonals.
# - If the conditions are satisfied, it marks the position as occupied, updates the arrays, and proceeds to the next column.
# - If all queens are placed successfully, it adds the current configuration to the result.
# - After completing the exploration of a column, it backtracks by undoing the changes made and explores other possibilities.
# - The time complexity of this approach is O(N!), as it explores all possible configurations.
# - The space complexity is O(N^2) to store the chessboard and the arrays to track availability.
