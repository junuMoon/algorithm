a = list(range(5))
print(a[::-1])
b =3

# 자료구조: 데이터 단위와 데이터 자체 사이의 물리적 또는 논리적인 관계

b = a.copy()
print(id(a))
print(id(b))
a.remove(2)
a.reverse()
print(a)
print(b)
