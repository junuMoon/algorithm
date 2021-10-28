n_case = int(input())
case_lst = []
for _ in range(n_case):
    case_lst.append(tuple(input().split(' ')))

# case1 = (3, 'ABC')
# case2 = (5, '/HTP')
# case_lst.append(case1)
# case_lst.append(case2)

for case in case_lst:
    result = ''.join(list(map(lambda i: i*int(case[0]), case[1])))
    print(result)


print(result)