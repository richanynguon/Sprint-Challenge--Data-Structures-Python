from doubly_linked_list import DoublyLinkedList

# https://en.wikipedia.org/wiki/Circular_buffer
# RingBuffer has two methods, `append` and `get`.
# The `append` method adds elements to the buffer. If capacity is reach the oldest el in ring will be old el = new el
# The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order.
# It should not return any `None` values in the list even if they are present in the ring buffer.

# _You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage  is less than capacity
        # then add new item to tail
        # make last item the current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def __len__(self):
        return self.storage.length

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = RingBuffer(capacity)
        for i in range(0, capacity):
            self.storage.append(None)

    def append(self, item):
        return self.storage.append(item)

    def get(self):
        return self.storage.get()

# https://stackoverflow.com/questions/27089682/python-typeerror-object-of-type-has-no-len

# *Stretch Goal*:  Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.  What are the advantages and disadvantages of using this method?  What disadvantage normally found in arrays is overcome with this arrangement?

# For example:

# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
