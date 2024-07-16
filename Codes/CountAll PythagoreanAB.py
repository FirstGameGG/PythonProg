import math

def find_pairs(c):
    count = 0
    a = 1
    while a < c:
        b = math.sqrt(c**2 - a**2)
        if b == int(b):
            count += 1
        a += 1
    return count // 2

c = int(input(''))
print(find_pairs(c))