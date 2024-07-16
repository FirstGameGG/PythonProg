def fibonacci(n, ch):
  fibo = []
  for i in range(n + 1):
    if i == 0 or i == 1:
      fibo.append(1)
    else:
      x = (fibo[i - 1] + fibo[i - 2])
      fibo.append(x)

  total = 0 
  i = 1   
  if ch == 'e':
    for num in fibo:
      if i % 2 == 0:
          total += num
      i += 1
  elif ch == 'o':
    for num in fibo:
      if i % 2 != 0:
          total += num
      i += 1
  return total



n = int(input())
ch = input().lower()
print(fibonacci(n, ch))