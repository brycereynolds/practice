
# I am not writing a heap from scratch here...
from heapq import heappush, heappop


class MinHeap:
    def __init__(self): self.h = []
    def __len__(self): return len(self.h)
    def push(self, val): return heappush(self.h, val)
    def pop(self): return heappop(self.h)
    def peek(self): return self.h[0]
    def peek_all(self): return self.h

class MaxHeap(MinHeap):
    def push(self, val): return heappush(self.h, -val)
    def pop(self): return -(heappop(self.h))
    def peek(self): return -(self.h[0]) if len(self.h) > 0 else 0
    def peek_all(self): return self.h

class MedianHeap:
    def __init__(self):
        self.min = MinHeap()
        self.max = MaxHeap()

    def peek_all(self):
        return self.min.peek_all() + self.max.peek_all()

    def push(self, val):
        if len(self.min) is 0:
            self.max.push(val)
        elif val > self.max.peek():
            self.min.push(val)
        else:
            self.max.push(val)

        return self.balance_heaps()

    def peek(self):
        if len(self.min) == len(self.max):
            return (self.min.peek() + self.max.peek()) / 2
        elif len(self.min) > len(self.max):
            return self.min.peek()
        else:
            return self.max.peek()

    def balance_heaps(self):
        if len(self.min) > len(self.max):
            self.max.push(self.min.pop())
        elif len(self.max) > len(self.min):
            self.min.push(self.max.pop())
        return self.peek()


heap = MedianHeap()
print(heap.push(12))
print(heap.peek_all())
print(heap.push(4))
print(heap.peek_all())
print(heap.push(5))
print(heap.peek_all())
print(heap.push(3))
print(heap.peek_all())
print(heap.push(8))
print(heap.peek_all())
print(heap.push(7))
print(heap.peek_all())
