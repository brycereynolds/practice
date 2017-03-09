#!/usr/bin/python

import math

# grid = [['b', 'd', '-', 'o', 'o'], ['-', 'd', 'o', 'o', 'o'], ['o', '-', '-', '-', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
# old_grid = [['d', 'b', 'o', '-', 'o'], ['-', 'd', '-', '-', '-'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]

# # replace any old_grid 'o' with values in grid

# # [[x if x != 'o' else y for (x, y) in zip(old_grid, grid)] (row, oldRow) for row in grid]

# flat_grid = [cell for row in grid for cell in row]
# flat_old_grid = [cell for row in old_grid for cell in row]

# flat_new_grid = [(y if x == 'o' or y == '-' or y == 'd' else x) for (x, y) in zip(flat_old_grid, flat_grid)]
# print(flat_new_grid)

# def slice_per(source, step):
#     return [source[i::step] for i in range(step)]

# new_grid = slice_per(flat_new_grid, 5)
# print(new_grid)


# with open('grid.txt', 'w') as f:
#     lines = [("".join(row) + "\n") for row in new_grid]
#     f.writelines(lines)
#     f.close()

# old_grid = [list(line.rstrip('\n')) for line in open('grid.txt', 'r')]
# print(old_grid)


print(math.log10(1))
print(math.log10(2))
print(math.log10(3))
print(math.log10(4))
print(math.log10(5))

print(math.pow(1, 2))
print(math.pow(2, 2))
print(math.pow(3, 2))
print(math.pow(4, 2))
print(math.pow(5, 2))

