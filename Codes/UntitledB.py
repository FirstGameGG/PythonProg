i = 1
while True:
    if i == 1000000:
        break
    if i % 10 == 0:
        print(i % 10)
    else:
        print(i % 10 ,end = '')
    i += 1