# Hash: 긁어모음, 뒤죽박죽, 가늘게 썬 고기 음식
# 시간과 공간의 트레이드-오프(상충관계)
# 충돌을 피하려면 해시 함수가 해시 테이블 크기(capacity)보다 작거나 같은 정수를 고르게 생성해야 함
# 따라서 해시 테이블의 크기는 소수를 선호함

from __future__ import annotations
from typing import Any, Type, Optional
import hashlib

class Node(object):
    def __init__(self, key: Any, value: Any, next_node: Optional[Node]) -> None:
        self.key = key
        self.value = value
        self.next_node = next_node

class HashChain(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_function(self, key: Any) -> int:
        """get hash value of key"""
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def get(self, key: Any) -> Any:
        """search element with key"""
        _hash = self.hash_function(key)
        p = self.table[_hash]

        while p is not None:
            if p.key == key:
                # return p.value
                print(p.value)
            p = p.next_node
        else:
            return None
    
    def put(self, key: Any, value: Any) -> None:
        """insert element with key and value"""
        _hash = self.hash_function(key)
        p = self.table[_hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next_node
        else:
            self.table[_hash] = Node(key, value, self.table[_hash])
        return True

    def delete(self, key: Any) -> None:
        """delete element with key"""
        _hash = self.hash_function(key)
        p = self.table[_hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[_hash] = p.next_node
                else:
                    pp.next = p.next_node
                return True
            else:
                pp = p
                p = p.next_node
            return False

    def dump(self) -> None:
        """dump hash table"""
        for i in range(self.capacity):
            p = self.table[i]
            while p is not None:
                print(p.key, p.value)
                p = p.next_node


if __name__ == '__main__':
    chain = HashChain(10)
    chain.put('a', 'a')
    chain.put('b', 'b')
    chain.put('7', 'c')
    chain.dump()
    
