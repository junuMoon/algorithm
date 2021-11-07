# 1부터 n까지 정수의 합 구하기

n = int(input())

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"{total=}")
print(f"{i=}")