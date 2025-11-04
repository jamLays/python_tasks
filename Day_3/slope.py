import math

x1, y1 = 2, 6
x2, y2 = 2, 10

m = y2-y1/x2-x1
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance)
print(m)
