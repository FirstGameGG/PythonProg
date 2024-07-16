

while True:
    n = int(input('Enter a number: '))
    if n == 0:
        break
    elif n < 0 or n == 1:
        print('Invalid input, try again.')
        continue
    else:
        i = 2
        is_prime = True
        while i < n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
            
        if is_prime == False:
            print('%d is not a prime number.' %(n))
        else:
            print('%d is a prime number.' %(n))        
                
print('End of program, goodbye.')