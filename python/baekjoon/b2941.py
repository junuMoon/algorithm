inputs = ['ljes=njak', 'ddz=z=', 'nljj', 'c=c=', 'dz=ak']
outputs = [6, 3, 3, 2, 3]

condition_dict = {
    'c': ['c=', 'c-'],
    'd': ['dz=', 'd-'],
    'l': ['lj'],
    'n': ['nj'],
    's': ['s='],
    'z': ['z='],
}


smp = 'ljes=njakddz=abnljj----dz===='
total = 0
while smp:
    check_lst = condition_dict.get(smp[0])
    if not check_lst:
        smp = smp[1:]
        total += 1
    else:
        checked = False
        for check in check_lst:
            if smp[0: len(check)] == check:
                print(f"special char: {smp[0:len(check)]}")
                smp = smp[len(check):]
                total += 1
                checked = True
        if not checked:
            smp = smp[1:]
            total += 1

print(total)
    

