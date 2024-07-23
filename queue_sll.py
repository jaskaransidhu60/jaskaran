# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a Queue using a Singly Linked List.

from sll import LinkedList, SLLException

class QueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def __str__(self):
        return str(self._list)

    def is_empty(self):
        return self._list.is_empty()

    def size(self):
        return self._list.length()

    def enqueue(self, value):
        self._list.insert_back(value)

    def dequeue(self):
        if self.is_empty():
            raise QueueException("Queue is empty")
        value = self._list._head.next.value
        self._list.remove_at_index(0)
        return value

    def front(self):
        if self.is_empty():
            raise QueueException("Queue is empty")
        return self._list._head.next.value

if __name__ == "__main__":
    # You can add your test cases here to validate the implementation
    pass
