# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a Queue using a Static Array.

class StaticArray:
    def __init__(self, size=4):
        self.size = size
        self.array = [None] * size

    def __str__(self):
        return str(self.array)

    def length(self):
        return self.size

class QueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self):
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["
        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa.array[front_index]) + ', '
            front_index = self._increment(front_index)
        if size > 0:
            out += str(self._sa.array[front_index])
        return out + ']'

    def is_empty(self):
        return self._current_size == 0

    def size(self):
        return self._current_size

    def print_underlying_sa(self):
        print(self._sa)

    def _increment(self, index):
        index += 1
        if index == self._sa.length():
            index = 0
        return index

    def enqueue(self, value):
        if self._current_size == self._sa.length():
            self._double_queue()
        self._back = self._increment(self._back)
        self._sa.array[self._back] = value
        self._current_size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueException("Queue is empty")
        value = self._sa.array[self._front]
        self._sa.array[self._front] = None
        self._front = self._increment(self._front)
        self._current_size -= 1
        return value

    def front(self):
        if self.is_empty():
            raise QueueException("Queue is empty")
        return self._sa.array[self._front]

    def _double_queue(self):
        new_sa = StaticArray(self._sa.length() * 2)
        index = self._front
        for i in range(self._current_size):
            new_sa.array[i] = self._sa.array[index]
            index = self._increment(index)
        self._sa = new_sa
        self._front = 0
        self._back = self._current_size - 1

if __name__ == "__main__":
    # You can add your test cases here to validate the implementation
    pass
