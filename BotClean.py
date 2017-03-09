#!/usr/bin/python

def nextMove(botRow, botCol, grid):
    if grid[botRow][botCol] == 'd':
        return 'CLEAN'

    # Brute force to find closest dirty cell next to bot - move towards that
    dirty = [(iCol, iRow) for iRow, row in enumerate(grid) for iCol, col in enumerate(row) if col == 'd']

    shortest = None
    shortestRow = None
    shortestCol = None

    for col, row in dirty:
        distance = abs(row - botRow) + abs(col - botCol)
        if shortest is None or (distance  < shortest):
            shortest = distance
            shortestRow = row
            shortestCol = col

    moveRow = shortestRow - botRow
    moveCol = shortestCol - botCol

    if moveRow < 0: return 'UP'
    if moveRow > 0: return 'DOWN'
    if moveCol < 0: return 'LEFT'
    if moveCol > 0: return 'RIGHT'

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    grid = [[j for j in input().strip()] for i in range(5)]
    print(nextMove(pos[0], pos[1], grid))
