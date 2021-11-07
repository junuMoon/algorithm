# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum: maximum = a[i]
    return maximum

if __name__ == '__main__':
    a = [1, 48, 27, 19, 88]
    print(f"{max_of(a)=}")

