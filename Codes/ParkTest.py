import math

hour = int(input("Enter number of hours: "))
minute = int(input("Enter number of minutes: "))
shop = int(input("Enter shopping amount: "))

if (hours < 0 or hours > 20) or (minutes < 0 or minutes > 59):
    print("Invalid time.")
else:
    time = hours + math.ceil(minutes / 60)
    if buyAmt >= 3001:
        amount = 0
    elif time <= 2:
        amount = 0
    elif time <= 4:
        if buyAmt >= 300 and buyAmt <= 3000:
            amount = 0
        else:
            amount = (time - 2) * 20
    else:
        if buyAmt >= 300 and BuyAmt <= 3000:
            amount = (time - 4) * 50
        else:
            amount = (time - 2) * 20 + (time - 4) * (50 - 20)
    
    if amount == 0:
        print("No charge, thank you.")
    else:
        print("Total amount due is %d Baht, thank you."%(amount))
