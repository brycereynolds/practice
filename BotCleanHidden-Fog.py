#!/usr/bin/python

class Cell:
    def __init__(self, col=0, row=0):
        self.col = col
        self.row = row

    def distance_to(self, target):
        return abs(self.row - target.row) + abs(self.col - target.col)

class GameManager:
    def __init__(self, bot=None):
        self.bot = bot

    def next_move_to(self, target):
        move_row = target.row - self.bot.row
        move_col = target.col - self.bot.col

        if move_row < 0: return 'UP'
        if move_row > 0: return 'DOWN'
        if move_col < 0: return 'LEFT'
        if move_col > 0: return 'RIGHT'

def next_move(botRow, botCol, grid):
    if grid[botRow][botCol] == 'd':
        return 'CLEAN'

    bot = Cell(botCol, botRow)
    game_manager = GameManager(bot)

    dirty = [(Cell(iCol, iRow)) for iRow, row in enumerate(grid) for iCol, col in enumerate(row) if col == 'd']
    hidden = [(Cell(iCol, iRow)) for iRow, row in enumerate(grid) for iCol, col in enumerate(row) if col == 'o']

    nearest_dirty = None
    nearest_hidden = None

    if len(dirty) > 0:
        for cell in dirty:
            if nearest_dirty is None or (cell.distance_to(bot) < nearest_dirty.distance_to(bot)):
                nearest_dirty = cell

        if nearest_dirty:
            return game_manager.next_move_to(nearest_dirty)

    # When we have no visible dirty cells - go exploring
    if len(hidden) > 0:
        for cell in hidden:
            if nearest_hidden is None or (cell.distance_to(bot) < nearest_hidden.distance_to(bot)):
                nearest_hidden = cell

        if nearest_hidden:
            return game_manager.next_move_to(nearest_hidden)


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    grid = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], grid))
