money = input()
isError = False
startcountdot = False
startcountcomma = False
countcomma = 0
countdot = 0
new = ''

if money.isnumeric():
     new = money
else:
     for num in money:
          if ',' in num:
               countcomma = 0
               startcountcomma = True
          elif '.' in num:
               new += num
               countdot = 0
               countcomma = 0
               startcountdot = True
          else:
               if num.isdigit():
                    new += num
                    countcomma += 1
                    if startcountdot == True:
                         countdot += 1
                    if startcountcomma == True:
                         countcomma += 1
               else:
                    isError = True
                    break
     
          if countcomma == 4 or countdot == 3 or money.count('.') > 1:
               isError = True
               break
          
if isError == True:
     print('ERROR')
else:
     if '.' not in new:
          print(int(new) + 1)
     else:
          print(float(new) + 1)
               
