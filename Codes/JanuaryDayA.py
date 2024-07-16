x = int(input())
n = int(input())

if (x < 1 or x > 7) or (n < 1 or n > 31):
  print('ERROR')

else:

  y = (n - x) % 7
  
  if y == 0:
    day = 'Sunday'
  elif y == 1:
    day = 'Monday'
  elif y == 2:
    day = 'Tuesday'
  elif y == 3:
    day = 'Wednesday'
  elif y == 4:
    day = 'Thursday'
  elif y == 5:
    day = 'Friday'
  elif y == 6:
    day = 'Saturday'  
    
    
  print(day)