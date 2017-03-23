import cProfile, pstats
from collections import deque
class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = [set() for x in range(n)]
    
    def connect(self, x, y):
        if x == y: return
        self.edges[x].add(y)
        self.edges[y].add(x)
    
    def _initialize_bfs(self):
        self.parent = [None] * self.nodes
        self.discovered = [False] * self.nodes
        self.distances = [-1] * self.nodes
    
    def _bfs(self, s):
        if len(self.edges[s]) == 0:
            return 
        
        self.distances[s] = 0
        q = deque()
        q.append(s)
        self.discovered[s] = True
        self.parent[s] = None
        while(len(q) > 0):
            temp = q.popleft()
            for neighbor in self.edges[temp]:
                if not self.discovered[neighbor]:
                    self.discovered[neighbor] = True
                    self.parent[neighbor] = temp
                    self.distances[neighbor] = 6 + self.distances[self.parent[neighbor]]
                    q.append(neighbor)
                    
    def find_all_distances(self, s):
        self._initialize_bfs()
        self._bfs(s)
        for i in range(self.nodes):
            if i != s:
                print(self.distances[i], end=" ")
        print("")


####### BELOW THIS LINE IS NOT SUBMITTED

# n,m = 3,1
# s = 2
# edges = [(2,3)]

# n,m = 4,2
# edges = [(1,2),(1,3)]

fname = 'algorithms/BFS_ShortestReachInGraph_input01.txt'
# fname = 'algorithms/BFS_ShortestReachInGraph_input02.txt'
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
    graph.find_all_distances(s-1)

    pr.disable()
    ps = pstats.Stats(pr).sort_stats('tottime')
    ps.print_stats()
