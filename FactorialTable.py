n = int(input('Enter a number: '))
i = 0

if n < 0:
    print('Invalid input, program terminates.')
else:
    while i <= n:
        print('%d! = ' %(i), end = '')
        j = 0   
        k = i
        count = 1    
    
        if k == 0:
            k = 1
            
        while j <= i:
            if k == 1:
                print('%d' %(k), end ='')
            if k > 1:
                print('%d x ' %(k), end ='')
                count *= k
            
            k -= 1
            j += 1
        
        print(' = %d' %(count))    
        i += 1
         