# https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&leftPanelTab=0
from math import *
from collections import *
from sys import *
from os import *

from typing import List


def setZeros(matrix: List[List[int]]) -> None:

    # rows = len(matrix)
    # cols = len(matrix[0])

    # matrix[0][j] is my column matrix
    # matrix[i][0] is my row matrix
    # But since the first element will colide
    # matrix[0][j][1:] is my column matrix and we have an extra element col0

    col0 = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:

                # for row
                matrix[i][0] = 0

                # for first column
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # We have to convert from the end (first row and col) are our markers
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    # Now we convert col markers as they are dependent on first row marker
    if matrix[0][0] == 0:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    # Now we convert first row
    if col0 == 0:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    return matrix
