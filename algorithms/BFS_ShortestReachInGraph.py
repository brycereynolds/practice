import cProfile, pstats
from collections import deque

class Graph:
    def __init__(self, n):
        self.nodes = n
        self._graph = {}
        self.EDGE_WEIGHT = 6

        for i in range(n):
            self._graph[i] = []

    def connect(self, u, v):
        # if u not in self._graph: return
        self._graph[u].append(v)
        self._graph[v].append(u)

    def find_all_distances(self, src):
        self._parents = [None] * self.nodes
        self._discovered = [False] * self.nodes
        self._distances = [-1] * self.nodes

        self.bfs_shortest_distance(src)

        return self._distances

    def bfs_shortest_distance(self, src):
        if len(self._graph[src]) == 0:
            return

        self._distances[src] = 0
        self._discovered[src] = True

        queue = deque()
        queue.append(src)
        while queue:
            current = queue.popleft()
            for child in self._graph[current]:
                if not self._discovered[child]:
                    self._discovered[child] = True
                    self._parents[child] = current
                    self._distances[child] = 6 + self._distances[current]
                    queue.append(child)


####### BELOW THIS LINE IS NOT SUBMITTED

# n,m = 3,1
# s = 2
# edges = [(2,3)]

# n,m = 4,2
# edges = [(1,2),(1,3)]

fname = 'BFS_ShortestReachInGraph_input01.txt'
# fname = 'BFS_ShortestReachInGraph_input02.txt'
# with open(fname) as f:
#     content = f.readlines()

pr = cProfile.Profile()
pr.enable()

infile = open(fname,"r")
for line in infile:
    n,m = [int(value) for value in next(infile).split()]

    pr = cProfile.Profile()
    pr.enable()

    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in next(infile).split()]
        graph.connect(x-1,y-1) 
    s = int(next(infile))
    distances = graph.find_all_distances(s-1)

    for i, val in enumerate(graph.find_all_distances(s-1)):
        if i != (s - 1):
            print(val, end=" ")
    print()


    pr.disable()
    ps = pstats.Stats(pr).sort_stats('ncalls')
    ps.print_stats()
