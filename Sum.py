ls = []
lssum = []
while True:
    x = int(input())
    if x == 0:
        break
    ls.append(x)

j = 0  
for num in ls:
    i = 0
    while i <= len(ls):
        l = ls[j:i]
        l = [int(x) for x in l]
        lssum.append(sum(l))
        i += 1
    j += 1
print(max(lssum))