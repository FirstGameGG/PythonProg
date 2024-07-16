money = input()
isError = False
startcountdot = False
startcountcomma = False
countcomma = 0
countdot = 0
new = ''
i = 0

if money.isnumeric():
     new = money
else:
     for num in money:
          if ',' in num:
               if startcountcomma == False:
                    if len(money[0:i]) > 3:
                         isError = True
                         break
                    if len(money[i + 1:]) < 3:
                         isError = True
                         break
               else:
                    if countcomma == 3:
                         countcomma = 0
                    else:
                         isError = True
                         break
               startcountcomma = True
               
          elif '.' in num:
               new += num
               countdot = 0
               if startcountcomma == True:
                    if countcomma < 3:
                         isError = True
                         break
               startcountdot = True
          else:
               if num.isdigit():
                    new += num
                    if startcountdot == True:
                         countdot += 1
                    if startcountcomma == True:
                         countcomma += 1
               else:
                    isError = True
                    break
          if countcomma > 3 or countdot > 2 or money.count('.') > 1:
               isError = True
               break
          i += 1

if isError == True:
     print('ERROR')
else:
     if '.' not in new:
          print(int(new) + 1)
     else:
          if countdot == 2:
               print('%.2f' %(float(new) + 1))
          else:
               print(float(new) + 1)