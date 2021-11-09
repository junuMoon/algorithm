from typing import Any, Sequence
import random

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    else:
        return -1

if __name__ == '__main__':
    num = 10
    x = [random.randint(1, 10) for _ in range(num)]
    key = 2
    idx = seq_search(x, key)
    print(x)
    print(idx)