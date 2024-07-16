count = 0
n = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

if (n < 0) and (digit < 0 or digit > 9):
  print("Invalid number.")
  print("Invalid digit.")
elif n < 0:
  print("Invalid number.") 
elif digit < 0 or digit > 9:
  print("Invalid digit.")
else:
  while n > 0:
    while True:
      x = n % 10
      if x == digit:
        count += 1
        
  n = n // 10

  print("Digit %d occurs %d times." %(digit, count))