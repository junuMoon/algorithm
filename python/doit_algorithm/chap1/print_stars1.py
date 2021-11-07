# *를 n개 출력하되 w개마다 줄바꿈하기

n = 15
w = 5

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print('')
if n % w:
    print()

print('---')

for _ in range(n // w):
    print('*' * w)
if (n % w):
    print('*' * (n % w))
