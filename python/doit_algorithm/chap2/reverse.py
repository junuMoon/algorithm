from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i -1], a[i]

if __name__ == '__main__':
    x = [1, 58, 28, 11, 99]
    reverse_array(x)

    for i in range(len(x)):
        print(f"x[{i}] = {x[i]}")

    x.reverse()
    print(x)
    print(list(x.__reversed__()))