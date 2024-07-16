text = input()
center = ''
ls1 = [x for x in text[:len(text) // 2]]
ls2 = [x for x in text[len(text) // 2:]]
if len(ls2) > len(ls1):
    center += ls2.pop(0)
    
ls1.reverse()
ls2.reverse()

str1 = ''.join(ls1)
print(str1, end = '')
if len(center) > 0:
    print(center, end = '')
str2 = ''.join(ls2)
print(str2)