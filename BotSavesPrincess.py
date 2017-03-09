#!/usr/bin/python
def displayPathtoPrincess(dimension, grid):
    moves = []

    def _appendMoves(direction, amount):
        for x in range(0, amount):
            moves.append(direction)

    distance = ((dimension - 1) // 2)

    if grid[0].find('p') != -1:
        if grid[0].find('p') == 0:
            _appendMoves('LEFT', distance)
        else:
            _appendMoves('RIGHT', distance)

        _appendMoves('UP', distance)
    else:
        if grid[dimension - 1].find('p') == 0:
            _appendMoves('LEFT', distance)
        else:
            _appendMoves('RIGHT', distance)

        _appendMoves('DOWN', distance)

    print('\n'.join(moves))


#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
