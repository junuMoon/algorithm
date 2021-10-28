smp1 = 'Mississipi'
smp2 = 'zZa'
smp3 = 'baaa'

def short(word):
    word = word.upper()
    count_set = sorted({*word}, key=word.count)
    *_, b, a = count_set
    
    if word.count(b) < word.count(a):
        print(a)
    else:
        print('?')
    result = word.split(',')
    return result[0]


def count_letter(word):
    result = {}
    for i in word:
        try:
            result[i] += 1
        except KeyError:
            result[i.upper()] = 1
    return result

word = 'hello'.upper()
count_dict = {c: word.count(c) for c in set()}

def dict_index(result):
    tmp = 0
    for k, v in result.items():
        if v > tmp:
            tmp = v
            max_ = list()
            max_.append(k)
        elif v == tmp:
            max_.append(k)
            
    return max_[0] if len(max_) == 1 else '?'

# print(dict_index(count_letter(smp1)))
# print(dict_index(count_letter(smp2)))
# print(dict_index(count_letter(smp3)))