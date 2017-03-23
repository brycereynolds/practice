# Second pass at this problem...

# After getting the hint to look at it as a basic BFS and recognize where the edges were,
# I was able to get a working solution in about 15 minutes.

"""
I'm seeing some pretty crazy solutions for this problem (Dijkstra's, Bellman Ford,
dynamic programming, etc.)

This is a straightforward BFS, and doesn't even require the explicit construction of
a graph, just an array with 100 (or 101) slots. For each slot, place either the index
of that slot (i.e. 5th spot has a 5 in it), or, if it has the head of a snake or
start of a ladder, the endpoint of that snake/ladder.

The slots form an implicit graph where the connected vertices from a given slot are the
6 slots after the current one.

Running a BFS on this implicit graph will get you the solution.
The reason you don't need dijkstra's is that you're only measuring the number of die
rolls: you don't care about distance travelled (edge weights). Similarly, you don't
need bellman ford as that is an algorithm needed to handle negative edge weights.
"""

"""
    link: https://www.hackerrank.com/challenges/the-quickest-way-up

    solution complexity:
        time: O(V + E) since every vertex and edge is explored in worst case
        space: O(V + E)
"""
from collections import deque, namedtuple

Pathway = namedtuple('Pathway', ['weight', 'tail'])
class Graph:
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node not in self._nodes:
            self._nodes += [node]

    def add_edge(self, edge):
        if edge[0] in self._nodes and edge[1] in self._nodes:
            if edge[0] not in self._edges:
                self._edges[edge[0]] = []
            self._edges[edge[0]] += [edge[1]]

    def bfs(self, target):
        q = deque()
        q.append(Pathway(1, self._nodes[0]))
        
        evaluated = []
        
        while q:
            path = q.popleft()

            if path.tail not in self._edges:
                continue

            for edge in self._edges[path.tail]:
                if edge is target:
                    return path.weight
                elif edge not in evaluated:
                    evaluated += [edge]
                    q.append(Pathway(path.weight + 1, edge))

        return -1

ladders={
    32:62,
    42:68,
    12:98
}

snakes = {
    95:13,
    97:25,
    93:37,
    79:27,
    75:19,
    49:47,
    67:17
}

ladders={
    5:6
}

snakes = {
    97:95
}

g = Graph()

squares = []
for i in range(1, 101):
    if i in ladders:
        squares += [ladders[i]]
    elif i in snakes:
        squares += [snakes[i]]
    else:
        squares += [i]
    g.add_node(squares[i - 1])

for square in g._nodes:
    for j in range(0, 6):
        if square + j < 100:
            g.add_edge((square, squares[square + j]))

print(g._edges)

print("BFS", g.bfs(100))