# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
from functools import reduce
from itertools import product

matrix =[
    [1,1,1,0,1],
    [0,0,1,0,0],
    [1,1,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,1,0],
]

def process_cell(matrix, row, col):
    if row < 0 or row >= len(matrix): return 0
    if col < 0 or col >= len(matrix[0]): return 0
    if matrix[row][col] is 0: return 0

    # Mark as visited
    matrix[row][col] = 0
    count = 1

    for x, y in product([-1, 0, 1], repeat=2):
        # (-1,-1), (-1,0), (-1,1), etc
        count += process_cell(matrix, row + x, col + y)

    return count

def process_matrix(matrix):
    count = 0
    for i in range(len(matrix)):
        if 1 not in matrix[i]: continue

        for j in range(len(matrix[i])):

            tmp = process_cell(matrix, i, j)
            if tmp and tmp > count: count = tmp
    return count


print(process_matrix(matrix))