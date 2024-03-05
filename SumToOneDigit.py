n = int(input())
while True:
    summ = 0    
    while True:
        if n == 0:
            break
        summ += n % 10
        n = n // 10
    if summ < 10:
        break
    else:
        n = summ
print(summ)