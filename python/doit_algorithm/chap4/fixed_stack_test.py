from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'clear', 'find', 'count', 'dump', 'exit'])

def select_menu() -> Menu:
    """Select Menu"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' | ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'current stack size: {len(s)} / {s.capacity}')
    m = select_menu()

    if m == Menu.push:
        x = int(input('push: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack is full')

    elif m == Menu.pop:
        try:
            print(s.pop())
        except FixedStack.Empty:
            print('stack is empty')

    elif m == Menu.peek:
        try:
            print(s.peek())
        except FixedStack.Empty:
            print('stack is empty')

    elif m == Menu.clear:
        s.clear()
        print('stack is cleared')

    elif m == Menu.find:
        x = int(input('find: '))
        if x in s:
            print(f'stack has {s.count(x)} [{x}](s), first index: {s.find(x)}')
        else:
            print(f'stack has no {x}')

    elif m == Menu.dump:
        s.dump()
    
    else:
        break


    