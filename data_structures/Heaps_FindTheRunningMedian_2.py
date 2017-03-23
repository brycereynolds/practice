from heapq import heappush, heappop

# Basically using maxheap on the left side to represent elements that are
# less than the effective median, and minheap on the right side for elements
# that are greater than the effective median.

# Heaps will differ in length by at most 1.

# When heaps are equal in length we take the mean of the heaps root elements.

# When the heaps are not balanced, we select the effective median from the
# root with the most elements.

class MinHeap:
    # parents <= children
    def __init__(self): self.h = []
    def __len__(self): return len(self.h)
    def push(self, val): heappush(self.h, val)
    def pop(self): return heappop(self.h)
    def peek(self): return self.h[0]
    def peek_all(self): return self.h

class MaxHeap(MinHeap):
    # parents >= children
    def push(self, val): heappush(self.h, -val)
    def pop(self): return -(heappop(self.h))
    def peek(self): return -(self.h[0])

class MedianHeap():
    def __init__(self):
        self.min = MinHeap()
        self.max = MaxHeap()

    def push(self, val):
        if len(self.max) > 0 and val > self.max.peek():
            self.min.push(val)
        else:
            self.max.push(val)

        self.balance_heaps()

        if(len(self.max) == len(self.min)):
            return (self.max.peek() + self.min.peek()) / 2.0

        return self.max.peek()

    def balance_heaps(self):
        if len(self.max) < len(self.min):
            self.max.push(self.min.pop())
        elif len(self.max) > len(self.min) + 1:
            self.min.push(self.max.pop())


median_heap = MedianHeap()
vals = [12, 4, 5, 4, 8, 7]

for val in vals:
    print("%.1f" % median_heap.push(val))
