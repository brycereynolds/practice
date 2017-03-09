#!/usr/bin/python
def nextMove(n,row,column,grid):
    count = 0
    for gridRow in grid:
        princess = gridRow.find('p')

        if princess != -1:
            if count < row:
                nextMove = 'UP'
            elif count == row:
                nextMove = 'LEFT' if princess < column else 'RIGHT'
            elif count > row:
                nextMove = 'DOWN'
        
        count += 1

    return nextMove

n = int(input())
row,column = [int(i) for i in input().strip().split()]
grid = []

for i in range(0, n):
    grid.append(input())

print(nextMove(n,row,column,grid))
