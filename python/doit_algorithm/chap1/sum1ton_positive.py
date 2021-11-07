# 1부터 n까지 정수의 합 구하기 (n은 양수)

while True:
    n = int(input())
    if n > 0:
        break

total = 0
for i in range(1, n+1):
    total += i

print(f"{total=}")
print(f"{i=}")
