#!/usr/bin/python

def nextMove(botRow, botCol, grid):
    if grid[botRow][botCol] == 'd':
        return 'CLEAN'

    # Brute force to find closest dirty cell next to bot - move towards that
    dirty = [(iCol, iRow) for iRow, row in enumerate(grid) for iCol, col in enumerate(row) if col == 'd']

    shortest = None
    moveUp = []
    moveDown = []
    moveLeft = []
    moveRight = []

    moveUpTotals = 0
    moveDownTotals = 0
    moveLeftTotals = 0
    moveRightTotals = 0

    for col, row in dirty:
        _row = row - botRow
        _col = col - botCol
        distance = abs(_row) + abs(_col)

        # Mark the most populated quadrants
        if _row < 0: moveUpTotals += 1
        if _row > 0: moveDownTotals += 1
        if _col < 0: moveLeftTotals += 1
        if _col > 0: moveRightTotals += 1

        if shortest is None or (distance  <= shortest):
            shortest = distance

            if _row < 0: moveUp.append([col, row])
            if _row > 0: moveDown.append([col, row])
            if _col < 0: moveLeft.append([col, row])
            if _col > 0: moveRight.append([col, row])


    # Look at all Totals - the one with the highest AND with a possible
    # move waiting - go there


    highestTotal = 0
    move = 'UNKNOWN'

    highestTotal, move = ((moveUpTotals, 'UP') if len(moveUp) > 0 and moveUpTotals > highestTotal else (highestTotal, move))
    highestTotal, move = ((moveDownTotals, 'DOWN') if len(moveDown) > 0 and moveDownTotals > highestTotal else (highestTotal, move))
    highestTotal, move = ((moveLeftTotals, 'LEFT') if len(moveLeft) > 0 and moveLeftTotals > highestTotal else (highestTotal, move))
    highestTotal, move = ((moveRightTotals, 'RIGHT') if len(moveRight) > 0 and moveRightTotals > highestTotal else (highestTotal, move))

    return move

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    print(nextMove(pos[0], pos[1], board))
