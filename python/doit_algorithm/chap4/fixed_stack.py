# LIFO: last in first out
from typing import Any


class FixedStack:
    """Stack with fixed capacity"""

    class Empty(Exception):
        """Raise when pop or peak to Empty FixedStack"""
        pass

    class Full(Exception):
        """Raise when push to Full FixedStack"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, item: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = item
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.stk = [None] * self.capacity
        self.ptr = 0

    def find(self, val: Any) -> Any:
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == val:
                return i
        return -1

    def count(self, val: Any) -> int:
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == val:
                cnt += 1
        return cnt

    def __contains__(self, value: Any) -> bool:
        return self.find(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print("Empty Stack")
        else:
            print(self.stk[:self.ptr])

            


