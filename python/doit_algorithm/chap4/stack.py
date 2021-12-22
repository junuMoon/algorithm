from typing import Any
from collections import deque

class Stack:
    """Fixed sized stack class(implemented with collection.deque)"""

    def __init__(self, capacity: int = 256) -> None:
        self.__stk = deque([], maxlen=capacity)
    
    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """Push value to stack"""
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        return self.__stk.clear()

    def find(self, value: Any) -> int:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.find(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print("Empty Stack")
        else:
            print(self.__stk)