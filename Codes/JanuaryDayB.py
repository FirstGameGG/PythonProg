x = input('')
n = int(input(''))

if (x == 'Sunday' or x == 'Monday' or x == 'Tuesday' or x == 'Wednesday' or x == 'Thursday' or x == 'Friday' or x == 'Saturday') and (n >= 1 and n <= 31):
    n = n - 1
    if x == 'Sunday':
        day = n % 7 
    elif x == 'Monday':
        day = (n + 1) % 7
    elif x == 'Tuesday':
        day = (n + 2) % 7
    elif x == 'Wednesday':
        day = (n + 3) % 7
    elif x == 'Thursday':
        day = (n + 4) % 7
    elif x == 'Friday':
        day = (n + 5) % 7
    elif x == 'Saturday':
        day = (n + 6) % 7
    
    if day == 0:
        print('Sunday')
    elif day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')    
        
else:
    print('ERROR')
    