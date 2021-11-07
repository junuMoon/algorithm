from max import max_of
import random

# number = 0
# x = []
# while True:
#     s = input(f'input x[{number}]: ')
#     if s == 'end':
#         break
#     x.append(int(s))
#     number += 1

# print(f'length of number {number}')
# print(f"{max_of(x)=}")

# num = 5
# x = [None] * num
# lo, hi = 3, 10

# for i in range(num):
#     x[i] = random.randint(lo, hi)

# print(f'{(x)}')
# print(f'{max_of(x)=}')

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', "AAC", "FLAC"]

print(f"{max_of(t)=}")
print(f"{max_of(s)=}")
print(f"{max_of(a)=}")