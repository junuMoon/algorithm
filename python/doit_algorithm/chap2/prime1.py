# 1,000 이하의 소수 나열하기

counter = 0

# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0:
#             break
#     else: print(n)
# print(f"{counter=}") # 78022

# 2부터 n-1까지 어떤 소수로도 나누어 떨어지지 않습니다
# counter = 0
# ptr = 0
# prime = [None] * 500

# prime[ptr] = 2
# ptr += 1

# for n in range(3, 1001, 2):
#     for i in range(1, ptr):
#         counter += 1
#         if n % prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1

# print(prime)
# print(f"{counter=}") # 14622

# n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않습니다
counter = 0
ptr = 0
prime = [None] * 255

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

print(prime)
print(f"{counter=}") # 3774