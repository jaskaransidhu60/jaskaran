# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a queue using a static array.

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

    def
