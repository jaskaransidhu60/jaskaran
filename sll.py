# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a Singly Linked List with various methods.

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLLException(Exception):
    pass

class LinkedList:
    def __init__(self, start_list=None):
        self._head = SLNode(None)
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self):
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self):
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self):
        return not self._head.next

    def insert_front(self, value):
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value):
        new_node = SLNode(value)
        node = self._head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length():
            raise SLLException("Index out of bounds")
        new_node = SLNode(value)
        node = self._head
        for _ in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def remove_at_index(self, index):
        if index < 0 or index >= self.length():
            raise SLLException("Index out of bounds")
        node = self._head
        for _ in range(index):
            node = node.next
        node.next = node.next.next

    def remove(self, value):
        node = self._head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return True
            node = node.next
        return False

    def count(self, value):
        count = 0
        node = self._head.next
        while node:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def find(self, value):
        node = self._head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def slice(self, start_index, size):
        if start_index < 0 or size < 0 or start_index + size > self.length():
            raise SLLException("Index out of bounds")
        sliced_list = LinkedList()
        node = self._head.next
        for _ in range(start_index):
            node = node.next
        for _ in range(size):
            sliced_list.insert_back(node.value)
            node = node.next
        return sliced_list

if __name__ == "__main__":
    # You can add your test cases here to validate the implementation
    pass
