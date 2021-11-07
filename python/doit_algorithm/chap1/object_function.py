# 함수 내부/외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1
def put_id():
    x = 1
    print(f"{id(x)=}")

print(f"{id(1)=}")
print(f"{id(n)=}")
put_id()

"""
id(1)=4306807088
id(n)=4306807088
id(x)=4306807088
"""

# n과 x는 이름에 불과하다
# namespaces에 저장
