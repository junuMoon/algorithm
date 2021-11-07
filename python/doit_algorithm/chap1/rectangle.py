area = 32

for i in range(1, area+1):
    if i * i > area: break
    if area % i: continue
    print(f"{i} * {area // i}")

