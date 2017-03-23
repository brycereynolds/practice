import math

class Heap:
    # heap that goes in increasing order on it's way down

    def __init__(self):
        self.nodes = []
        self.size = 0

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def get_parent_index(self, index):
        return (index - 1) / 2

    def parent(self, index):
        return self.nodes[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        tmp = self.nodes[index_two]
        self.nodes[index_two] = self.nodes[index_one]
        self.nodes[index_one] = tmp

    def add(self, val):
        self.nodes.append(val)
        self.size += 1
        self.bubble_up()

    def bubble_up(self):
        index = self.size - 1

        # If my current index is smaller than my parent, swap us then ask again
        while(self.has_parent(index) and self.nodes[index] < self.parent(index)):
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    def bubble_down(self):
        pass

    def peek(self):
        return self.nodes[0]

    def peek_all(self):
        return self.nodes

    def median(self):
        val = None
        if self.size is 1:
            val = self.nodes[0]
        elif self.size % 2 is 1:
            val = self.nodes[int(math.floor(self.size / 2))]
        else:
            left = self.nodes[(self.size / 2) - 1]
            right = self.nodes[(self.size / 2 + 1) - 1]
            val = (left + right) / 2

        return float(val)


vals = [12, 4, 5, 3, 8, 7]

heap = Heap()
for val in vals:
    heap.add(val)
    print(heap.peek_all())
    print(heap.median())