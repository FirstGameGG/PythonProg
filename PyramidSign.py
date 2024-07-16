x = 5
i = 1
while x > 0:
  print(' ' * (x - 1), end = '')
  if i == 1:
    print('$')
  if i > 1:
    print('$ ' * i)
  x -= 1
  i += 1