text = input()
i = 1
ls1 = [x for x in text[:(len(text) // 2 )]]
ls2 = [x for x in text[len(text) // 2:]]
ls2.reverse()

if len(ls2) > len(ls1):
    ls1.append(ls2.pop())
while True:
    if len(ls1) == 0 or len(ls2) == 0:
        break    
    print(ls1.pop(0), end = '')
    print(ls2.pop(0), end = '')
    
if len(ls1) > 0:
    print(ls1.pop())