#x1, s = input().split()

#x2 = int(s) * 2 - int(x1)

#print(x2)

mylist = []

for x in range(10):
    mylist.append(int(input()) % 42)
    
myset = set(mylist)

print(len(myset))
    
