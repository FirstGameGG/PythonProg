amount = int(input())
guess = int(input())
target = int(input())
i = 0
copy_target = target
position_count = 0
count = 0
near = 0

while guess > 0:
    x = guess % 10
    j = 0
    while target > 0:
        y = target % 10
        if y == x:
            count += 1
        if y == x and i == j:
            position_count += 1
            count -= 1
        if (y == x + 1 or y == x - 1) and i == j:
            near += 1
        target = target // 10
        j += 1 
        
    target = copy_target
    guess = guess // 10
    i += 1

if position_count == 1:
    m = 1
elif position_count == 2:
    m = 3
elif position_count == 3:
    m = 6
else:
    m = 0
    
if position_count == 1 and count == 2:
    m = m + 0.8
    
if near >= 1:
    m = m + (near * 0.3)


print(amount * m)