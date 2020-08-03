# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_tail(self, value):
#         new_node = Node(value, None)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.size = 0

    def idx(self, index):
        return (index + 1) % len(self.storage)

    # def __str__(self):
    #     return self.capacity

    def append(self, item):
        self.storage[self.head]= item
        self.head = self.idx(self.head)
        if self.size < len(self.storage):
            self.size +=1

    def get(self):
        return self.storage[:self.size]

# buffer = RingBuffer(3)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())
# print(buffer)
