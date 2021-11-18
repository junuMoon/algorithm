from enum import Enum
from chained_hash import HashChain

Menu = Enum('Menu', ['추가','삭제','검색','모두_출력','종료'])

def select_munu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='     ')
        n = int(input('메뉴를 선택하세요: '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash_chain = HashChain(13)

while True:
    menu = select_munu()
    if menu == Menu.추가:
        key = int(input('key: '))
        value = input('value: ')
        if not hash_chain.put(key, value):
            print('Failed in Adding')

    elif menu == Menu.삭제:
        key = int(input('key: '))
        if not hash_chain.delete(key):
            print('Failed in Removing')

    elif menu == Menu.검색:
        key = int(input('key: '))
        t = hash_chain.get(key)
        if t is None:
            print('Not Found')
        else:
            print(f'Found: {t}')

    elif menu == Menu.모두_출력:
        hash_chain.dump()

    else:
        break


