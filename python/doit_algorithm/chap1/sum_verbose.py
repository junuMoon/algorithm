# a부터 b까지 정수의 합 (for)
a, b = 3, 8

if a>b:
    a, b = b, a

total = 0
for i in range(a, b+1):
    print(f"{i} + ", end="")
    total += i

print(f"{i} = ", end="")
print(f"{total}")