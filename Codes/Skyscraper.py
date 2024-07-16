import math
count = 0
max_height = -math.inf
while True:
    height = int(input())
    if height == -1:
        break
    if height > max_height:
        count = count + 1
        max_height = height
print(count)