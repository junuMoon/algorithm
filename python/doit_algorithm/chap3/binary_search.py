from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """Binary search element that match the key in sequence a."""
    pl = 0
    pr = len(a) -1

    while True:
        print(pl, pr)
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc -1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    a = [1, 8, 19, 28, 33, 54, 65, 98]
    key = 18
    idx = bin_search(a, key)

# 이진 검색 알고리즘은 반복할 때마다 검색 범위가 거의 절반으로 줄어드므로
# 필요한 비교횟수는 평균 log N
# 검색에 실패할 경우는 [log(N+1)]
# 검색에 성공할 경우는 log(N)-1