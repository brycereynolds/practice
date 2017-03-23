from pprint import pprint
from collections import namedtuple

Count = namedtuple('Count', ['coin','count'])


"""

http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

1. Optimal Substructure

To count the total numbe of solutions, we can divide all set solutions in two sets:
    - Solutions that do not contain mth coin (or Sm)
    - Solutions that contain at least one Sm

Let count(S[], m, n) be the function to count the number of solutions, then it can be written as sum of:

count(S[], m - 1, n) 
count(S[], m, n - Sm)

"""

def count(S, m, n):

    # If n is 0 then this is 1 solution (do not include any coin)
    if n is 0:
        return 1

    # If n is less than 0, then no solution exists
    if n < 0:
        return 0

    # If there are no coins and n is greater than 0, then no solution exists
    if m <= 0 and n >= 1:
        return 0

    # count is sum of solutions (i) including S[m - 1] (ii) excluding S[m - 1]
    # n - (value of last coin)
    # 
    return count(S, m - 1, n) + count(S, m, n - S[m - 1])




coins = [2, 5, 3, 6]
n = 10

# coins = [1]
# target = 1

print(count(coins, len(coins), target))

