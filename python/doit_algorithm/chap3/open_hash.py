from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Bucket:
    """a hash is composed of buckets"""
    def __init__(self, key: Any = None,
                        value: Any = None,
                        status: Status = Status.EMPTY):
        self.key = key
        self.value = value
        self.status = status

    def set(self, key: Any, value: Any, status: Status) -> None:
        """Set attributes"""
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status) -> None:
        """Set status of bucket"""
        self.status = status


class OpenHash:
    """Open hash table"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.buckets = [Bucket() for _ in range(capacity)]

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Bucket:
        hashed = self.hash_value(key)
        p = self.buckets[hashed]

        for _ in range(self.capacity):
            if p.status == Status.EMPTY and p.key == key:
                break
            elif p.status == Status.OCCUPIED and p.key == key:
                return p
            hashed = self.rehash_value(hashed)
            p = self.buckets[hashed]

        return None

    def search(self, key: Any) -> Any:
        """Search for key in hash table"""
        p = self.search_node(key)
        if p is not None:
            return p.value
        return None

    def insert(self, key: Any, value: Any) -> None:
        """Insert key and value into hash table"""
        if self.search(key) is not None:
            return False 

        hashed = self.hash_value(key)
        p = self.buckets[hashed]
        for _ in range(self.capacity):
            if p.status in [Status.EMPTY, Status.DELETED]:
                p.set(key, value, Status.OCCUPIED)
                break
            hashed = self.rehash_value(hashed)
            p = self.buckets[hashed]
        return False

    def delete(self, key: Any) -> None:
        """Delete key from hash table"""
        p = self.search_node(key)
        if p is not None:
            p.set_status(Status.DELETED)
            return True
        return False

    

