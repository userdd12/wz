# Implementation of Circular Queue (using Python lists)

class CircularQueue:
    """ Circular queue with fixed capacity """

    def __init__(self, n: int):
        self.n = n
        self.array = [None] * self.n
        self.front = 0  # index of the first element
        self.rear = 0
        self.size = 0

    def __len__(self) -> int:
        """
        >>> cq = CircularQueue(5)
        >>> len(cq)
        0
        >>> cq.enqueue("A")
        >>> len(cq)
        1
        """
        return self.size

    def is_empty(self) -> bool:
        """
        >>> cq = CircularQueue(5)
        >>> cq.is_empty()
        True
        >>> cq.enqueue("A")
        >>> cq.is_empty()
        False
        """
        return self.size == 0

    def first(self):
        """
        >>> cq = CircularQueue(5)
        >>> cq.first()
        False
        >>> cq.enqueue("A")
        >>> cq.first()
        'A'
        """
        return False if self.is_empty() else self.array[self.front]

    def enqueue(self, data):
        """
        This function insert an element in the queue using self.rear value as an index
        >>> cq = CircularQueue(5)
        >>> cq.enqueue("A")
        >>> (cq.size, cq.first(), cq.last())
        1, 'A', 'A'
        >>> cq.enqueue("B")
        >>> (cq.size, cq.first(), cq.last())
        2, 'A', 'B'
        """
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data
        self.rear = (self.rear+1)%self.n
        self.size += 1
        return self

    def dequeue(self):
        """
        This function removes an element from the queue using on self.front value as an
        index
        >>> cq = CircularQueue(5)
        >>> cq.dequeue()
        False
        >>> cq.enqueue("A")
        >>> cq.enqueue("B")
        >>> cq.dequeue()
        'B'
        >>> (cq.size, cq.first(), cq.last())
        1, 'A', 'A'
        >>> cq.dequeue()
        False
        """
        if self.size == 0:
            raise Exception ("UNDERFLOW")

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1)%self.n
        self.size -= 1
        return temp
