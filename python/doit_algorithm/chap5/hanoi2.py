# Tower of Hanoi
# 1. move 1 ~ n-1 disks from pilar1 to pilar2
# 2. move n disk from pilar1 to pilar3
# 3. move 1 ~ n-1 disks from pilar2 to pilar3

# def move(no, from_p, to_p):
#     if no == 1:
#         print(f"move disk {no} from {from_p} to {to_p}")
#         return
#     else:
#         move(no-1, from_p, 6 - from_p - to_p)
#         print(f"move disk {no} from {from_p} to {to_p}")
#         move(no-1, 6 - from_p - to_p, to_p)

# n = 4
# move(n, 1, 3)

from stack import Stack


n = 3

def get_from_pilar(n):
    from_p = Stack(n)
    for i in range(n, 0, -1):
        from_p.push(i)
    return from_p






