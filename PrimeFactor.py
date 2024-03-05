n = int(input('Enter positive integer: '))
i = 2

if n <= 0:
    print('Invalid number.')
elif n == 1:
    pass
else:
    while i * i <= n:
        while n % i == 0:
            print(i)
            n //= i
            
        i += 1
        
    if n > 1:
        print(n)
        