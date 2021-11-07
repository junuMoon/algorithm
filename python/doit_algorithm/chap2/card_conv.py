# 10진수 정숫값을 입력받아 2~36 진수로 변환하여 출력

def card_conv(x: int, r: int) -> str:
    """정수 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열 반환"""

    d = ''
    dchar = '01234566789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print(f"{card_conv(16, 5)=}")