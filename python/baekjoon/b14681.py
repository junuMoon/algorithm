point = list()
point.append(int(input()))
point.append(int(input()))

if point[0] > 0:
    quadrant = 1
    if point[1] < 0:
        quadrant = 4
else:
    quadrant = 2
    if point[1] < 0:
        quadrant = 3
    
print(quadrant)

