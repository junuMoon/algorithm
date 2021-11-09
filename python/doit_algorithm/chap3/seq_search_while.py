# 선형검색: Linear Search
from typing import Any, Sequence
import random
from copy import deepcopy

def seq_search(seq: Sequence, key: Any) -> int:
    """Sequence A에서 Key와 값이 같은 원소를 선형 검색(while)"""
    a = deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i
    
if __name__ == '__main__':
    num = 10
    x = random.sample(range(50), 10)
    key = 2
    idx = seq_search(x, key)
    print(x)
    print(idx)