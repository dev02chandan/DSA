from typing import List


def sudokuSolver(board: List[List[int]]) -> bool:

    # Function to check if there are duplicates in the subgrid
    def has_duplicates_in_subgrid(board, row, col):
        mylist = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4),
                  (4, 7), (7, 1), (7, 4), (7, 7)]
        offset = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
        temp = []
        for mid1, mid2 in mylist:
            for dr, dc in offset:
                r, c = mid1 + dr, mid2 + dc
                if board[r][c] != 0:
                    temp.append(board[r][c])
            if len(set(temp)) != len(temp):
                return True
            else:
                temp = []
        return False

    # Function to find the next empty spot
    def findNextEmptySpot(i, j):
        for row in range(i, len(board)):
            for col in range(j, len(board[0])):
                if board[row][col] == 0:
                    return row, col
        return False, False

    # Function to check if a number can be placed in the current spot
    def possiblePlacement(number, i, j):
        if number in board[i]:
            return False

        column = [row[j] for row in board]
        if number in column:
            return False

        offset = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

        for dr, dc in offset:
            r, c = i + dr, j + dc
            if board[r][c] == number:
                return False

        return True

    # Recursive helper function to solve the Sudoku puzzle
    def recursiveHelper(i, j):
        row, col = findNextEmptySpot(i, j)
        if row is False:
            return True

        for number in range(1, 10):
            if possiblePlacement(number, row, col):
                board[row][col] = number

                # Find the next empty spot in the same 3x3 subgrid
                next_i = (row // 3) * 3
                next_j = (col // 3) * 3
                if recursiveHelper(next_):
                    return True
                else:
                    board[row][col] = 0

        return False

    # Check for duplicates in rows and columns
    for row in board:
        row = [x for x in row if x != 0]
        if len(row) != len(set(row)):
            return False

    for col, column_vals in enumerate(zip(*board)):
        column_vals = list(column_vals)
        column_vals = [x for x in column_vals if x != 0]
        if len(column_vals) != len(set(column_vals)):
            return False

    # Check for duplicates in subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if has_duplicates_in_subgrid(board, i, j):
                return False

    # Solve the Sudoku puzzle using recursion
    if recursiveHelper(0, 0):
        return True
    else:
        return False


'''
6 7 8 2 1 4 5 0 8 
8 5 4 2 1 9 0 7 3 
9 7 3 0 6 8 1 2 4 
3 8 5 0 4 2 7 6 9 
0 4 0 9 5 6 8 3 1 
6 0 0 0 3 7 2 4 5 
0 3 6 0 0 0 9 5 2 
7 2 1 0 9 5 3 8 6 
5 0 8 0 2 3 4 1 7 

this test case is failing
expected output: True
'''
