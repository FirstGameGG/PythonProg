import math

n = int(input())
minn = math.inf
y = 1

while y <= n:
    
    x = n
    while True:
        if x == 0:
            break
        if x * y == n:
            if x + y < minn:
                minn = x + y
            
        x -= 1
    y += 1
    
print(minn)