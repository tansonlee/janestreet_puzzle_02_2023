import math
import random

def intersects(cx, cy, cr):
    return cx + cr >= 1 or cx - cr <= 0 or cy + cr >= 1 or cy - cr <= 0

def circle_from(p1x, p1y, p2x, p2y):
    cx = (p1x + p2x) / 2
    cy = (p1y + p2y) / 2
    cr = math.dist([p1x, p1y], [p2x, p2y]) / 2
    return cx, cy, cr

def simulate():
    p1x = random.random()
    p1y = random.random()
    p2x = random.random()
    p2y = random.random()

    cx, cy, cr = circle_from(p1x, p1y, p2x, p2y)
    if intersects(cx, cy, cr):
        return True
    return False

count = 100000000
success = 0

for _ in range(count):
    if simulate():
        success += 1

print(success / count)
