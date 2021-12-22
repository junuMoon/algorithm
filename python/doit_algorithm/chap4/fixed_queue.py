from typing import Any

class FixedQueue:

    class Empty(Exception):
        """Raise when pop or peak to Empty FixedQueue"""
        pass

    class Full(Exception):
        """Raise when push to Full FixedQueue"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """Initialize queue with fixed capacity"""
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        """Return length of queue"""
        return self.no

    def is_empty(self) -> bool:
        """Return True if queue is empty"""
        return self.no <= 0

    def is_full(self) -> bool:
        """Return True if queue is full"""
        return self.no >= self.capacity

    def enque(self, value: Any) -> None:
        """Push value to queue"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self) -> Any:
        """Pop value from queue"""
        if self.is_empty():
            raise FixedQueue.Empty
        value = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return value

    def peek(self) -> Any:
        """Return value at front of queue"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> int:
        """Find value in queue and return index"""
        for i in range(self.no):
            idx = i + self.front % self.capacity
            if self.que[idx] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        """Count value in queue"""
        cnt = 0
        for i in range(self.no):
            idx = i + self.front % self.capacity
            if self.que[idx] == value:
                cnt += 1
        return cnt

    def __contains__(self, value: Any) -> bool:
        """Return True if queue contains value"""
        return self.find(value) >= 0

    def clear(self) -> None:
        """Clear queue"""
        self.no = 0
        self.front = 0
        self.rear = 0

    def dump(self) -> None:
        """Print queue"""
        if self.is_empty():
            print("Empty Queue")
        else:
            print(self.que[self.front:self.rear])

