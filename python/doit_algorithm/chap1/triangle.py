# 왼쪽 아래가 직각인 이등변 삼각형 * 로 출력하기

n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print('')

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()

