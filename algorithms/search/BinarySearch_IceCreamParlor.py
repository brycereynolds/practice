import cProfile, pstats
from collections import namedtuple

IceCream = namedtuple('IceCream', ['orig_index', 'cost'])

class Parlor:
    """ Parlor handles purchasing ice creams from a list of available ice creams
    submitted during initialization. It always internally sorts it's ice creams
    based on price but maintains a relationship to the original index that the
    ice cream was submitted as.
    """
    def __init__(self, ice_creams):
        self.ice_creams = [IceCream(orig_index + 1, cost) for orig_index, cost in enumerate(ice_creams)]
        self.ice_creams.sort(key=lambda ice_creams: ice_creams.cost)

    def __len__(self):
        return len(self.ice_creams)

    def __getitem__(self, i):
        return self.ice_creams[i]

    def purchase(self, funds, left, right):
        """ Binary search in disguise:
        We always purchase the most valuable ice-cream you can afford.
        Once purchased an ice cream is out of stock.
        """
        if left > right: return None

        mid = (left + right) // 2

        # print(self.ice_creams[mid])

        if funds == self.ice_creams[mid].cost:
            choice = self.ice_creams[mid]
            del self.ice_creams[mid]
            return choice
        elif funds < self.ice_creams[mid].cost:
            return self.purchase(funds, left, mid - 1)
        else:
            return self.purchase(funds, mid + 1, right)



def find_ice_creams(total_funds, ice_creams):
    parlor = Parlor(ice_creams)
    pick1, pick2 = None, None
    money = total_funds - 1

    while money > 0:
        match = parlor.purchase(money, 0, len(parlor) - 1)
        if match is None:
            if pick1 is None:
                money -= 1
            else:
                # We failed to find a matching pair for pick1
                # Reset this pick and deduct funds by one to
                # reset our original search.
                money = pick1.cost - 1
                pick1 = None

        elif pick1 is None:
            # have a match
            pick1 = match
            money = total_funds - match.cost
        elif pick2 is None:
            pick2 = match
            break;

    return (pick1, pick2)


############ INPUT HANDLING FOR HACKERRANK

# total_funds = 890
# # arr = [1, 4, 5, 3, 2]
# # arr = [2,2,4,3]
# arr = [286, 461, 830, 216, 539, 44, 989, 749, 340, 51, 505, 178, 50, 305, 341, 292, 415, 40, 239, 950, 404, 965, 29, 972, 536, 922, 700, 501, 730, 430, 630, 293, 557, 542, 598, 795, 28, 344, 128, 461, 368, 683, 903, 744, 430, 648, 290, 135, 437, 336, 152, 698, 570, 3, 827, 901, 796, 682, 391, 693, 161, 145]

# fname = 'CtciIceCreamParlor_input00.txt'
fname = 'CtciIceCreamParlor_input02.txt'
with open(fname) as f:
    content = f.readlines()

pr = cProfile.Profile()
pr.enable()

for i in range(1, len(content), 3):
    total_funds = int(content[i].strip())
    n = int(content[i + 1].strip())
    ice_creams = list(map(int, content[i + 2].strip().split(' ')))

    # pr = cProfile.Profile()
    # pr.enable()

    (pick1, pick2) = find_ice_creams(total_funds, ice_creams)

    if pick1 is None or pick2 is None:
        print("NO MATCH")
    else:
        _ = sorted([pick1.orig_index, pick2.orig_index])
        print('{0} {1}'.format(_[0], _[1]))

    # pr.disable()
    # ps = pstats.Stats(pr).sort_stats('tottime')
    # ps.print_stats()
