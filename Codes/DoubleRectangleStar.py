height = int(input('Enter height: '))
width = int(input('Enter width: '))
i = 1
j = 0

if height <=0 or width <= 0:
    print('Invalid input, program terminates.')
else:
    while i <= height:
        j = 0
        while j <= width:
            if j == width:
                print()
                break
            if i % 2 != 0:
                print('* ',end='')
            else:
                print(' *',end='')
            j += 1
        i += 1
                
