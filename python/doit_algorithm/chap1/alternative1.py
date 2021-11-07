# +와 -를 번갈아 출력하기

n = 4

for i in range(n):
    if i % 2:
        print('-', end='')
    else: print('+', end='')
print('')

for _ in range(n // 2):
    print('+-', end='')
if n % 2:
    print('+', end='')
print('')