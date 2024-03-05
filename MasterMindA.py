position_count = 0
count = 0
target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
copy_target = target
i = 0
j = 0
        
while guess > 0:
    x = guess % 10
    j = 0
    while target > 0:
        y = target % 10
        if y == x:
            count += 1
        if y == x and i == j:
            position_count += 1
            count -= 1
        target = target // 10
        j += 1 
        
    target = copy_target
    guess = guess // 10
    i += 1

if position_count == 4:
    print('Congratulations, you just mastered my mind!!')
else:  
    if position_count == 0:
        pos_correct = 'No positions correct'
    elif position_count == 1:
        pos_correct = 'One position correct'
    elif position_count == 2:
        pos_correct = 'Two positions correct'
    elif position_count == 3:
        pos_correct = 'Three positions correct'    
   
    if count == 0:
        dig_correct = 'no digits correct'
    elif count == 1:
        dig_correct = 'one digit correct'
    elif count == 2:
        dig_correct = 'two digits correct'
    elif count == 3:
        dig_correct = 'three digits correct' 
    elif count == 4:
        dig_correct = 'four digits correct'    
    print('%s, %s'%(pos_correct, dig_correct))       
