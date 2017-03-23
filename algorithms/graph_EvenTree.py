"""
link: https://www.hackerrank.com/challenges/even-tree
time:
space:

Find the maximum number of edges you can remove from the tree to get a forest such that
each connected component of the forest contains an even number of vertices.
"""
class Graph():
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node not in self._nodes:
            self._nodes += [node]

    def add_edge(self, edge):
        if edge[0] not in self._edges:
            self._edges[edge[0]] = []
        self._edges[edge[0]] += [edge[1]]

        if edge[1] not in self._edges:
            self._edges[edge[1]] = []
        self._edges[edge[1]] += [edge[0]]

    # Given "maximum" we probably want some DP techniques
    def max_even_tree(self):
        self._cuts = 0
        self._max_even_tree(1)
        return self._cuts

    def _max_even_tree(self, root, path=[]):
        if root not in self._nodes:
            return 0

        if root not in self._edges:
            return 0

        path = path + [root]

        count = 0
        for child in self._edges[root]:
            if child in path:
                continue

            count += 1

            child_count = self._max_even_tree(child, path)

            if (child_count + 1) % 2 is not 0:
                count += child_count
            else:
                self._cuts += 1

        return count



nodes = 10
edges = [(2,1),(3,1),(4,3),(5,2),(6,1),(7,2),(8,6),(9,8),(10,8)]
# nodes = 4
# edges = [(1,2),(1,3),(3,4)]

g = Graph()

for i in range(nodes):
    g.add_node(i + 1)

for edge in edges:
    g.add_edge(edge)

print(g._nodes)
print(g._edges)

print(g.max_even_tree())