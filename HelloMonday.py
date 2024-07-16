day = int(input())
hour = int(input())
minute = int(input())

if day < 1 or day > 7:
    pass
else:
    if day == 1:
        day = 'sunday'
    elif day == 2:
        day = 'monday' 
    elif day == 3:
        day = 'tuesday' 
    elif day == 4:
        day = 'wednesday' 
    elif day == 5:
        day = 'thursday'
    elif day == 6:
        day = 'friday' 
    elif day == 7:
        day = 'saturday'
    
    if (hour > 23 or hour < 0) or (minute > 59 or minute < 0):
        pass
    else:
        time = (hour * 60) + minute    
        if time > 240 and time <= 720:
            greeting = 'good-morning'   
        elif time > 720 and time <= 1080:
            greeting = 'good-afternoon'
        elif time > 1080 and time <= 1320:
            greeting = 'good-evening'
        elif (time > 1320 and time <= 1439) or (time <= 240 and time >= 0):
            greeting = 'good-night'
    
        print('{}-{}.png'.format(greeting, day))