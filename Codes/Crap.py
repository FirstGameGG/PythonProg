count = 0
isbreak = False

while True:
    if isbreak == True:
        break
    
    a = int(input())
    b = int(input())
    count += 1
    
    if (a > 6 or a < 1) or (b > 6 or b < 1):
        print('ERROR')
        count -= 1
        continue
    else:
        target = a + b
        if a + b == 7 or a + b == 11:
            result = 'W'
            break
        elif a + b == 2 or a + b == 3 or a + b == 12:
            result = 'L'
            break
        else:
            while True:
                c = int(input())
                d = int(input())
                count +=1
                
                if (c > 6 or c < 1) or (d > 6 or d < 1):
                    print('ERROR')
                    count -= 1
                    continue  
                
                if c + d == target:
                    result = 'W'
                    isbreak = True
                    target = c + d
                    break
                    
                if c + d == 7:
                    result = 'L'
                    isbreak = True
                    target = c + d
                    break
                
print('{} {} {}'.format(count, target, result))