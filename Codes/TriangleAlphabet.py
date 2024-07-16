def change_to_abc(number: int):
    result = ''
    i = 0
    while i < number:
        result += chr(ord('A') + i)
        i += 1
    return result

n = int(input('Enter a number: '))
i = 1

if n <= 0 or n > 26:
    print('Invalid input, program terminates.')
else:
    while i <= n:
        output = change_to_abc(i)
        print(output)
        i += 1 
        
    i = n - 1
    while i > 0:
        output = change_to_abc(i)
        print(output)
        i -= 1         