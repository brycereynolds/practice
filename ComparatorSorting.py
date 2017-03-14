# See: https://www.hackerrank.com/challenges/ctci-comparator-sorting

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return repr(self.name, self.score)
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            if a.name < b.name:
                return - 1
            else:
                return 1
        else:
            return 1



# Another way to solve it that is super slick...

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def comparator(a, b):
        # See https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
        return -1 if (a.score, b.name) > (b.score, a.name) else 1
