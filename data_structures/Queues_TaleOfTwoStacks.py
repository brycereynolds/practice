# I could use collections.deque but am using two stacks for demonstration purposes
class Queue():
    def __init__(self):
        self._inbox = []
        self._outbox = []

    def peek(self):
        if len(self._outbox) > 0:
            return self._outbox[-1]
        elif len(self._inbox) > 0:
            return self._inbox[0]
        else:
            return None

    def pop(self):
        if len(self._outbox) == 0:
            while len(self._inbox) > 0:
                self._outbox += [self._inbox.pop()]

        return self._outbox.pop()

    def put(self, value):
        self._inbox += [value]


q = Queue()
q.put(12)
q.put(15)
q.put(17)

print(q.peek())
print(q.peek())

q.put(17)
q.put(18)

print(q.peek())

print("POP", q.peek(), q.pop())

print(q.peek())

q.put(20)

print(q.peek())

print("POP", q.peek(), q.pop())
