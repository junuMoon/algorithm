smp = 'backjoon'
# smp = input()
alphabet = range(97, 123)

result = ' '.join(list(map(lambda i: str(smp.find(chr(i))), alphabet)))
# print(smp_list). 
print(result)


