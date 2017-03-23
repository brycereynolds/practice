from pprint import pprint
from collections import namedtuple, deque

"""
The top section covers the basic ideas of graphs. Below I implement a more structured class.

Very simple conceptual implementation of DFS

Our graph w/out a data structure:

A -> B
A -> C
B -> C
B -> D
C -> D
D -> C
E -> F
F -> C

Our data consists of nodes A - F a total of 8 edges.

Our graph represented by a data structure where each key represents
a node, each edge is captured in a list:
"""
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D','E','F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print("graph data:")
pprint(graph)

print("\n\n======== SIMPLE FUNCTIONS ========")
def has_path(graph, start, end, path=[]):
    if start not in graph:
        return None

    path = path + [start]

    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            new_path = has_path(graph, node, end, path)
            if new_path: return new_path

    return None

print("has_path => {0}".format(has_path(graph, 'A', 'D')))

def all_paths(graph, start, end, path=[]):
    if start not in graph:
        return []

    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths += [new_path]

    return paths

print("all_paths => {0}".format(all_paths(graph, 'A', 'D')))


def shortest_path(graph, start, end, path=[]):
    if start not in graph:
        return None

    path = path + [start]

    if start == end:
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

    return shortest


print("shortest_path => {0}".format(shortest_path(graph, 'A', 'D')))

print("\n\n======== CLASS IMPLEMENTATION ========")

Edge = namedtuple('Edge', ['start', 'end'])
class Graph:

    """ Think of graphs as a collection of nodes and edges (or arcs) connecting
    those nodes. These connections may be one-way or bi-directional dependent
    upon the specification outlined.

    """
    def __init__(self, graph={}):
        self._graph = graph

    @property
    def graph(self):
        return self._graph

    @property
    def nodes(self):
        return list(self._graph.keys())

    @property
    def edges(self):
        """Return list of edge tuples (start, end) where
        order indicates direction.
        """
        edges = []
        for node in self._graph:
            for child in self._graph[node]:
                if (node, child) not in edges:
                    edges.append(Edge(node, child))
        return edges

    def add_node(self, node, children=[]):
        """ If the node "node" is not in the graph,
        a key "node" with an empty list as a value is
        added to the dictionary.

        Otherwise nothing has to be done. 
        """
        if node not in self._graph:
            self._graph[node] = []

    def add_edge(self, start, end):
        """Only adds an edge if we have the parent node
        "start" and this edge does not already exist on
        this parent node.

        Otherwise nothing has to be done. 
        """
        if start in self._graph:
            if end not in self._graph[start]:
                self._graph[start].append(end)


    ##### ALGORITHM SEARCH METHODS #####

    def dfs(self, src, dest, path=[]):
        """
        Recursive algorithm. Goes deep into children first. Make sure to use an
        is_visited flag of some sort (we are accomplishing that here by checking
        that child does not exist in the current walked path).
        """
        if dest not in self._graph or src not in self._graph:
            return None

        # We are intentionally creating a new path here while extending what existed
        path = path + [src]

        if src == dest:
            return path

        for child in self._graph[src]:
            if child not in path:
                new_path = self.dfs(child, dest, path)
                if new_path is not None:
                    return new_path

        return None

    def bfs(self, src, dest):
        """
        A non-recursive algorithm that instead uses queues. Push current onto the queue
        then process queue. If that is not found to be a match then push current's
        children onto the queue and continue.
        """
        if dest not in self._graph or src not in self._graph:
            return None

        visited = []
        queue = deque(src)

        while queue:
            current = queue.popleft()
            visited.append(current)

            if current == dest:
                return True

            for child in self._graph[current]:
                if child not in visited:
                    queue.append(child)

    def bfs_all_paths(self, src, dest):
        if dest not in self._graph or src not in self._graph:
            return None

        paths = []
        queue = deque([[src]])

        while queue:
            current_path = queue.popleft()
            current = current_path[-1]

            if current == dest:
                paths.append(current_path)

            for child in self._graph[current]:
                if child not in current_path:
                    new_path = current_path + [child]
                    queue.append(new_path)
        return paths

    # This could also just wrap bfs_all_paths but in this implementation
    # we can remove any path that is already larger than our shortest
    def bfs_shortest_path(self, src, dest):
        if dest not in self._graph or src not in self._graph:
            return None

        shortest = None
        paths = []
        queue = deque([[src]])

        while queue:
            current_path = queue.popleft()
            if shortest and len(current_path) > shortest:
                continue

            current = current_path[-1]

            if current == dest:
                if shortest is None or len(current_path) <= shortest:
                    shortest = len(current_path)
                    paths.append(current_path)

            for child in self._graph[current]:
                if child not in current_path:
                    new_path = current_path + [child]
                    queue.append(new_path)
        return paths


g = Graph(graph)
print("g.nodes")
pprint(g.nodes)
print("g.edges")
pprint(g.edges)

g.add_node('J')
pprint(g.nodes)

print("add edges")
g.add_edge('J', 'A')
g.add_edge('J', 'J')
pprint(g.edges)

print("\n\n======== SEARCH ALGORITHMS ========")

print("g.dfs('A', 'D') => {0}".format(g.dfs('A','D')))
print("g.dfs('A', 'J') => {0}".format(g.dfs('A','J')))

print("\nBy adding a connection that is deep for the A-J test we should show that this is indeed depth first...")
print("g.add_edge('D', 'J') => {0}".format(g.add_edge('D', 'J')))
print("g.dfs('A', 'J') => {0}".format(g.dfs('A','J')))

print("g.add_edge('A', 'J') => {0}".format(g.add_edge('A', 'J')))

print("\nEven though we just added a new edge which is shorter, we will still get our long edge since it is an earlier child in A's list:")
print("g.dfs('A', 'J') => {0}".format(g.dfs('A','J')))

print("\nBFS should solve this 'goes deep first' problem that is found in DFS search:")
print("g.bfs('A', 'J') => {0}".format(g.bfs('A','J')))
print("g.dfs('A', 'J') => {0}".format(g.dfs('A','J')))

pprint(g.graph)

print("g.bfs_all_paths('A', 'J') => {0}".format(g.bfs_all_paths('A','J')))
print("g.bfs_shortest_path('A', 'J') => {0}".format(g.bfs_shortest_path('A','J')))
print("g.bfs_shortest_path('A', 'D') => {0}".format(g.bfs_shortest_path('A','D')))
