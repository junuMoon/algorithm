# a부터 b까지 정수의 합 (for)
a, b = 3, 8

if a>b:
    a, b = b, a

total = 0
for i in range(a, b+1):
    if i < b:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")
    total += i

print(f"{total}")