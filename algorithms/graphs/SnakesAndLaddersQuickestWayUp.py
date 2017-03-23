# INCOMPLETE

# Didn't finish. Got a solution that finds the first path just using ladders in about 45 minutes. After that I went to the discussion board to try and get some minor hints.

# I'm following a hint and moving to my second pass (see graph_SnakesAndLaddersQuickestWayUp_2.py)

"""
    link: https://www.hackerrank.com/challenges/the-quickest-way-up

    solution complexity:
        time:
        space:
"""


def closest_to_target(paths, target):
    top = None

    for path in paths:
        if path[1] > target: continue

        if not top:
            top = path
        elif die_cost(path[1], target) < die_cost(top[1], target):
            top = path

    return top

def die_cost(current, target):
    n = target - current
    return int((n // 6) + 1 if n % 6 > 0 else n / 6)

def shortest_path(ups, downs, location, target):
    if location == target:
        return

    path = closest_to_target(ups, target)

    if path:
        path[0] - location
        cost = die_cost(path[1], target)

        jump_cost = shortest_path(ups, downs, location, path[0])
        if jump_cost:
            cost += jump_cost
        return cost
    else:
        return die_cost(location, target)







tests = 2

ladders=[(32,62),(42,68),(12,98)]
snakes = [(95,13),(97,25),(93,37),(79,27),(75,19),(49,47),(67,17)]

ladders = [(8,52),(6,80),(26,42),(2,72)]
snakes = [(51,19),(39,11),(37,29),(81,3),(59,5),(79,23),(53,7),(43,33),(77,21)]


print(shortest_path(ladders, snakes, 1, 100))