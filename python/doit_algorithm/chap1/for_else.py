# 10-99 난수 생성(13이 나오면 중단)
import random

n = 5

for _ in range(n):
    r = random.randint(10, 20)
    print(r, end=' ')
    if r == 13:
        print()
        print('하림이 똑똑해')
        break
else:
    print('\nTerminate the process')