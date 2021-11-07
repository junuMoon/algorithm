# 세 정수를 입력받아 중앙값 구하기1

def med3(a, b, c):
    """ a, b, c의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif c > b:
        return b
    else:
        return c
        
def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환"""
    if (b>=a and a>=c) or (b<=a and c>=a):
        return a
    elif (a>b and b>c) or (b>a and c>b):
        return b
    return c

print(f"{med3(1, 2, 3)=}")
print(f"{med3(1, 3, 2)=}")
print(f"{med3(2, 1, 3)=}")
print(f"{med3(2, 3, 1)=}")
print(f"{med3(3, 2, 1)=}")
print(f"{med3(3, 1, 2)=}")
