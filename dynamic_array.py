# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@gmail.com
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 22 July
# Description: Implementation of a dynamic array.

class DynamicArray:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.array = [None] * size

    def __str__(self):
        return str(self.array[:self.count])

    def append(self, value):
        if self.count == self.size:
            self._resize()
        self.array[self.count] = value
        self.count += 1

    def _resize(self):
        self.size *= 2
        new_array = [None] * self.size
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array

    def length(self):
        return self.count

    def get_at_index(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set_at_index(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        self.array[index] = value

if __name__ == "__main__":
    # Add any necessary test cases to verify your implementation
    pass
