n = int(input(''))
i = 10
x = 0

if n > 0:
    while  i < (n * 10):
        x = int(((n % i) - x) / (i / 10))
        print(x)
        i = i * 10
else:
    print('ERROR')
    