phone = range(1, 11)
time_phone = range(2, 12)

def proc1(num):
    return time_phone[num-1]

# num = 868242
# num_list = list(map(int, list(str(num))))
# num_time_list = list(map(proc1, num_list))
# print(sum(num_time_list))

num_str_map = {'abc': 3,
                'def': 4,
                'ghi': 5,
                'jkl': 6,
                'mno': 7,
                'pqrs': 8,
                'tuv': 9,
                'wxyz': 10}
num_str_map2 = {}
for k, v in num_str_map.items():
    num_str_map2[k.upper()] = v

print(num_str_map2)

num_str = 'WA'

total = 0 
for i in num_str:
    for k, v in num_str_map2.items():
        if i in k:
            print(k, v)
            total += v
            break

print(total)



# inputs = ['WA', 'UNUCIC']
# outpus = [13, 36]