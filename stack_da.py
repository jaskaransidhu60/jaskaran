# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a Stack using a Dynamic Array.

from dynamic_array import DynamicArray

class StackException(Exception):
    pass

class Stack:
    def __init__(self):
        self._da = DynamicArray()

    def __str__(self):
        return "STACK: " + str(self._da)

    def is_empty(self):
        return self._da.length() == 0

    def size(self):
        return self._da.length()

    def push(self, value):
        self._da.append(value)

    def pop(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        value = self._da.get_at_index(self.size() - 1)
        self._da.set_at_index(self.size() - 1, None)
        self._da.count -= 1
        return value

    def top(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da.get_at_index(self.size() - 1)

if __name__ == "__main__":
    # You can add your test cases here to validate the implementation
    pass
