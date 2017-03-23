def compare_points(list_one, list_two):
    one = 0
    two = 0
    for i, val in enumerate(list_one):
        if val > list_two[i]:   one += 1
        elif val < list_two[i]: two += 1

    return [one, two]

alice = [5,6,7]
bob = [3,6,10]

points = compare_points(alice, bob)
print('{0} {1}'.format(*points))