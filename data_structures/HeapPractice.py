# class Heap:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = None



class Heap:
    def __init__(self):
        self.nodes = []
        self.size = 0

    def get_left_child_index(self, parent):
        return 2 * parent + 1

    def get_right_child_index(self, parent):
        return 2 * parent + 2

    def get_parent_index(self, child):
        return (child - 1) / 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.nodes[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.nodes[self.get_right_child_index(index)]

    def parent(self, index):
        return self.nodes[self.get_parent_index(index)]

    def peek(self):
        if self.size is 0:
            return False

        return self.nodes[0]

    def peek_all(self):
        return self.nodes

    def poll(self):
        if self.size is 0:
            raise False

        head = self.nodes[0]
        self.nodes[0] = self.nodes.pop()
        self.size -= 1

        self.bubble_down()
        return head

    def add(self, val):
        self.nodes.append(val)
        self.size += 1
        self.bubble_up()

    def bubble_up(self):
        index = self.size - 1
        while(self.has_parent(index) and self.parent(index) > self.nodes[index]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def bubble_down(self):
        index = 0
        while(self.has_left_child(index)):
            smallerChildIndex = self.get_left_child_index(index)
            if(self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
                smallerChildIndex = self.get_right_child_index(index)

            if self.nodes[index] < self.nodes[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex


    def swap(self, index_one, index_two):
        value_one = self.nodes[index_one]
        self.nodes[index_one] = self.nodes[index_two]
        self.nodes[index_two] = value_one





a = Heap()
a.add(23)
a.add(12)
a.add(14)
a.add(11)
a.add(15)
a.add(35)
a.add(2)

print(a.peek())
print(a.peek_all())

a.poll()
print(a.peek_all())

