#!/usr/bin/python
import os.path

class GameManager:
    def __init__(self, bot=None, grid=None):
        self.save_path = 'grid.txt'
        self.bot = bot
        self.save_grid(grid)

    def next_move_to(self, target):
        if target.row == self.bot.row:
            return 'RIGHT' if target.col > self.bot.col else 'LEFT'
        return 'DOWN' if target.row > self.bot.row else 'UP'

    def find_cells(self, value):
        return [(Cell('DIRTY', iCol, iRow)) for iRow, row in enumerate(self.grid) for iCol, col in enumerate(row) if col == value]

    def save_grid(self, grid):
        old_grid = []
        if os.path.exists(self.save_path):
            old_grid = [list(line.rstrip('\n')) for line in open(self.save_path, 'r')]

        new_grid = grid if len(old_grid) == 0 else self.priority_merge_grid(old_grid, grid)

        # Save new grid to file for later use...
        with open(self.save_path, 'w') as f:
            lines = [("".join(row) + "\n") for row in new_grid]
            f.writelines(lines)
            f.close()

        self.grid = new_grid

    def priority_merge_grid(self, grid_a, grid_b):
        flat_grid_a = [cell for row in grid_a for cell in row]
        flat_grid_b = [cell for row in grid_b for cell in row]

        # If old grid has a 'o', replace it with new grid value (may be 'o' or something new...)
        flat_new_grid = [(y if x == 'o' or y == '-' or y == 'd' or y == 'b' else x) for (x, y) in zip(flat_grid_a, flat_grid_b)]
        merged = [flat_new_grid[i:i+5] for i in range(0, len(flat_new_grid),5)]
        return merged

class Cell:
    def __init__(self, cellType, col=0, row=0):
        self.type = cellType
        self.col = col
        self.row = row

    def distance_to(self, target):
        return abs(self.row - target.row) + abs(self.col - target.col)

def next_move(botRow, botCol, grid):
    if grid[botRow][botCol] == 'd':
        return 'CLEAN'

    bot = Cell('BOT', botCol, botRow)
    game_manager = GameManager(bot, grid)

    dirty = game_manager.find_cells('d')
    nearest_dirty = None

    if len(dirty) > 0:
        for cell in dirty:
            if nearest_dirty is None or (cell.distance_to(bot) < nearest_dirty.distance_to(bot)):
                nearest_dirty = cell

        if nearest_dirty:
            return game_manager.next_move_to(nearest_dirty)

    # When we have no visible dirty cells - go exploring
    hidden = game_manager.find_cells('o')
    nearest_hidden = None

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
