# SLNode.py
class SLNode:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None

# LinkedList.py
class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass

class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True if list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #
    def insert_front(self, value: object) -> None:
        """
        Insert a new node at the front of the linked list
        """
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        Insert a new node at the back of the linked list
        """
        new_node = SLNode(value)
        node = self._head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a new node at the specified index in the linked list
        """
        if index < 0 or index > self.length():
            raise SLLException("Index out of bounds")
        new_node = SLNode(value)
        node = self._head
        for i in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        Remove the node at the specified index in the linked list
        """
        if index < 0 or index >= self.length():
            raise SLLException("Index out of bounds")
        node = self._head
        for i in range(index):
            node = node.next
        node.next = node.next.next

    def remove(self, value: object) -> bool:
        """
        Remove the first occurrence of the value in the linked list
        """
        node = self._head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return True
            node = node.next
        return False

    def count(self, value: object) -> int:
        """
        Count the occurrences of the value in the linked list
        """
        count = 0
        node = self._head.next
        while node:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def find(self, value: object) -> bool:
        """
        Find if the value exists in the linked list
        """
        node = self._head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Slice the linked list starting from start_index to start_index + size
        """
        if start_index < 0 or size < 0 or start_index + size > self.length():
            raise SLLException("Invalid start index or size")
        sliced_list = LinkedList()
        node = self._head
        for i in range(start_index):
            node = node.next
        for i in range(size):
            node = node.next
            sliced_list.insert_back(node.value)
        return sliced_list

if __name__ == "__main__":
    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
    print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
    print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")


# stack_da.py
from dynamic_array import DynamicArray

class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Stack:
    def __init__(self):
        """
        Initialize new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        Add a new value to the top of the stack
        """
        self._da.append(value)

    def pop(self) -> object:
        """
        Remove and return the top element from the stack
        """
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da.pop()

    def top(self) -> object:
        """
        Return the top element from the stack without removing it
        """
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da[self._da.length() - 1]

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


# queue_sa.py
from static_array import StaticArray

class QueueException(Exception):
    """
    Custom exception to be used by Queue class.
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["
        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)
        if size > 0:
            out += str(self._sa[front_index])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty, False otherwise.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def print_underlying_sa(self) -> None:
        """
        Print underlying StaticArray. Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(self._sa)

    def _increment(self, index: int) -> int:
        """
        Move index to next position.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0
        return index

    # ---------------------------------------------------------------------- #
    def enqueue(self, value: object) -> None:
        """
        Add a new value to the back of the queue
        """
        if self._current_size == self._sa.length():
            self._double_queue()
        self._back = self._increment(self._back)
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """
        Remove and return the front element from the queue
        """
        if self.is_empty():
            raise QueueException("Queue is empty")
        value = self._sa[self._front]
        self._front = self._increment(self._front)
        self._current_size -= 1
        return value

    def front(self) -> object:
        """
        Return the front element from the queue without removing it
        """
        if self.is_empty():
            raise QueueException("Queue is empty")
        return self._sa[self._front]

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit. #
    def _double_queue(self) -> None:
        """
        Double the size of the queue when full
        """
        new_sa = StaticArray(self._sa.length() * 2)
        for i in range(self._current_size):
            new_sa[i] = self._sa[self._front]
            self._front = self._increment(self._front)
        self._sa = new_sa
        self._front = 0
        self._back = self._current_size - 1

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# Basic functionality tests #")
    print("\n# enqueue()")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue()")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for _ in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)
    q.print_underlying_sa()

    print("\n# front()")
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
        print(q)

    print("\n# Circular buffer tests: #\n")
    def action_and_print(header: str, action: callable, values: [], queue: Queue) -> None:
        """
        Print header, perform action,
        then print queue and its underlying storage.
        """
        print(header)
        if values:
            for value in values:
                action(value)
        else:
            action()
        print(queue)
        queue.print_underlying_sa()
        print()

    q = Queue()
    print("# Enqueue: 2, 4, 6, 8")
    test_case = [2, 4, 6, 8]
    for value in test_case:
        q.enqueue(value)
    print(q)
    q.print_underlying_sa()
    print()

    action_and_print("# Dequeue a value", q.dequeue, [], q)
    action_and_print("# Enqueue: 10", q.enqueue, [10], q)
    action_and_print("# Enqueue: 12", q.enqueue, [12], q)

    print("# Dequeue until empty")
    while not q.is_empty():
        q.dequeue()
    print(q)
    q.print_underlying_sa()
    print()

    action_and_print("# Enqueue: 14, 16, 18", q.enqueue, [14, 16, 18], q)
    action_and_print("# Enqueue: 20", q.enqueue, [20], q)
    action_and_print("# Enqueue: 22, 24, 26, 28", q.enqueue,
                     [22, 24, 26, 28], q)
    action_and_print("# Enqueue: 30", q.enqueue, [30], q)


# stack_sll.py
from SLNode import SLNode

class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        Add a new value to the top of the stack
        """
        new_node = SLNode(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> object:
        """
        Remove and return the top element from the stack
        """
        if self.is_empty():
            raise StackException("Stack is empty")
        value = self._head.value
        self._head = self._head.next
        return value

    def top(self) -> object:
        """
        Return the top element from the stack without removing it
        """
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


# queue_sll.py
from SLNode import SLNode

class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------
    def enqueue(self, value: object) -> None:
        """
        Add a new value to the back of the queue
        """
        new_node = SLNode(value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        Remove and return the front element from the queue
        """
        if self.is_empty():
            raise QueueException("Queue is empty")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return value

    def front(self) -> object:
        """
        Return the front element from the queue without removing it
        """
        if self.is_empty():
            raise QueueException("Queue is empty")
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
        print(q)
