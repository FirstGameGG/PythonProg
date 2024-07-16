def mixname(t1, t2):
    vowels = 'aeiou'
    count = 0
    newt1 = ''
    newt2 = ''
    isFinished1 = False
    isFinished2 = False
    for i in t1:
        if i in vowels:
            count += 1
            
        if count < 2:
            newt1 += i
        else:
            isFinished1 = True
    if isFinished1 == False: newt1 = t1
    count = 0        
    for i in t2:
        if count >= 1:
            newt2 += i
            isFinished2 = True
        if i in vowels:
            count += 1
    if isFinished2 == False: newt2 = t2
    newname = newt1 + newt2
    return newname

name1 = input()
name2 = input()
print(mixname(name1, name2))
        
            
    