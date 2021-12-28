from copy import copy
from stack import Stack

order = 0
def recur(n: int) -> int:
    global order 
    order += 1
    cur_order = copy(order)
    if n > 0:
        recur(n-1)
        print(order, cur_order, n)
        recur(n-2)


# implement recur in non-recursive way

def recur1a(n: int) -> int:
    """remove tail recursive func"""
    while n > 0:
        recur1a(n-1)
        print(n)
        n = n-2

# remove recursion from fucntion with stack
def recur1b(n: int) -> int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n -= 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n -= 2
            continue
        break
