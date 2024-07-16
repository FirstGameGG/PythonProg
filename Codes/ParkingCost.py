import math
n = 0
amount = 0
hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))

if (hours < 0 or hours > 20) or (minutes < 0 or minutes > 59):
    print("Invalid time.")
else:
    times = hours + math.ceil(minutes / 60)
    if times > 20:
        print("Invalid time.")
    else:
        while n <= times:
            if buyAmt >= 3001:
                break
            if n >= 5:
                amount += 50
            if n == 3 or n == 4:
                if buyAmt >= 300 and buyAmt <= 3000:
                    pass
                else:
                    amount += 20
            if n <= 2:
                pass
    
            n += 1
    
        if amount == 0:
            print("No charge, thank you.")
        else:
            print("Total amount due is %d Baht, thank you."%(amount))