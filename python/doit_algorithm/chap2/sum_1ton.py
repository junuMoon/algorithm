# 1~n 정수의 합

from typing import Sequence

def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s = 0
    while n:
        s += n
        n -= 1
    return s

x = 10
print(f"sum of (1, {x}) -> {sum_1ton(x)=}")

# aoroqustn n값을 sum_1ton 함수 안에서 변경했는데도
# 실제 인수 x의 값이 변경되지 않는 것은 int가 immutable 타입이기 때문
# 변수 n의 값이 업데이트 되는 시점에 다른 객체를 참조하게 됨
# 함수를 종료할 때 n이 참조하는 곳은 정수 0

def sum_2ton(n: Sequence) -> int:
    print('before')
    print(id(n), id(x[2]))
    n[2] = 3
    print('after')
    print(id(n), id(x[2]))

    return sum(n)

def foo_mutable(bar: Sequence) -> None:
    bar[1] = 2

def foo_immutable(bar: int) -> None:
    bar = 2

x = [1, 5, 10]
foo_mutable(x)
print(x)
x = 4
foo_immutable(x)
print(x)

# print(id(x), id(x[2]))
# print(f"sum of {x} -> {sum_2ton(x)=}")
# print(id(x), id(x[2]))

# 파이썬에서 인수 전달은 실제 인수인 객체에 대한 참조를 값으로 전달하여
# 매개변수에 대입되는 방식입니다. 다른 프로그래밍 언어에서는 실제 인수의 값을
# 매개변수에 복사하는 값에 의한 호출(Call by Value)을 사용하거나,
# 실제 인수의 참조를 매개변수에 복사하여 매개변수가 실제 인수와 같아지는
# 참조에 의한 호출(Call by Reference)를 사용합니다
# 하지만 파이썬에서는 이 2가지 호출의 중간적인 방식으로 참조하는 값을 전달합니다
# 객체 참조에 의한 전달(Call by Object Reference):
# 함수의 실행 시작 시점에서 매개변수는 실제 인수와 같은 객체를 참조합니다
# 함수에서 매개변수의 값을 변경하면 인수의 형(type)에 따라 다음과 같이 구분합니다
# 1. 인수가 Immutable: 함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고
# 그 객체에 대한 참조로 업데이트 됨. 따라서 매개변수의 값을 변경해도 호출하는 쪽의
# 실제 인수에는 영향을 주지 않음
# 2. 인수가 Mutable: 함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트함.
# 따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경

