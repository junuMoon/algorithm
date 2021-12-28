# Tower of Hanoi
# Pilar는 Stack을 상속한다
# Pilar에는 disk가 ascending order로 쌓인다
# 1번 Pilar의 모든 disk를 3번 pilar로 옮겨라

from stack import Stack
from typing import Any



class Pilar(Stack):

    class NewDiskIsGreaterThanLastDisk(Exception):
        pass

    def __init__(self, n, start_pilar=True):
        super().__init__(n)
        if start_pilar:
            self.get_disks(n)

    def get_disks(self, n):
        for i in range(n, 0, -1):
            self.push(i)

    def check_disk_order(self, disk):
        if self.is_empty():
            return 
        if self.peek() < disk:
            raise Pilar.NewDiskIsGreaterThanLastDisk

    def push(self, value: Any) -> None:
        self.check_disk_order(value)
        return super().push(value)

def get_pilars(n_pilar, n_disk):
    pilars = []
    for i in range(n_pilar):
        start_pilar = True if i == 0 else False
        pilars.append(Pilar(n=n_disk, start_pilar=start_pilar))
    return pilars

# solution
# 1. move 1 ~ n-1 disks from from_p to other_p
# 2. move n disk from from_p to to_p
# 3. move 1 ~ n-1 disks from other_p to to_p

def move_disk(from_p, to_p, pilars):
    disk = pilars[from_p].pop()
    pilars[to_p].push(disk)
    print(f'Move disk {disk} from {from_p} to {to_p}')

def move_tower(n_disk, from_p, to_p, pilars):
    other_p = sum(range(len(pilars))) - from_p - to_p
    if n_disk == 1:
        move_disk(from_p, to_p, pilars)
    else:
        move_tower(n_disk - 1, from_p, other_p, pilars)
        move_disk(from_p, to_p, pilars)
        move_tower(n_disk - 1, other_p, to_p, pilars)

def solution(n_pilar=3, n_disk=3, from_p=0, to_p=2):
    assert from_p != to_p
    assert to_p <= n_pilar - 1
    pilars = get_pilars(n_pilar, n_disk)
    move_tower(n_disk, from_p, to_p, pilars)

    pilars[0].dump()
    pilars[-1].dump()
    

if __name__ == '__main__':
    solution()



