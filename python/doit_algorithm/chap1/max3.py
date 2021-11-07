# 세 정수를 입력받아 최댓값 구하기

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c
print(f"maximum: {maximum}")

# 알고리즘: 어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차
