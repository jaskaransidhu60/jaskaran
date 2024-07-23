# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a Stack using a Singly Linked List.

from sll import LinkedList, SLLException

class StackException(Exception):
    pass

class Stack:
    def __init__(self):
        self._list = LinkedList()

    def __str__(self):
        return str(self._list)

    def is_empty(self):
        return self._list.is_empty()

    def size(self):
        return self._list.length()

    def push(self, value):
        self._list.insert_front(value)

    def pop(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        value = self._list._head.next.value
        self._list.remove_at_index(0)
        return value

    def top(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._list._head.next.value

if __name__ == "__main__":
    # You can add your test cases here to validate the implementation
    pass
