minn = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")
dohomework = False
days = round((minn / 60) / 24)

if days < 2:
  dohomework = True
if days > 5:
  dohomework = False

if temp > 40 or (temp > 25 and rain == 'Y'):
  dohomework = False

print(">>> %d days before due" %(days))
if dohomework == True:
  print(">>> I will do the assignment.")         
else:
  print(">>> I will not do the assignment.")  