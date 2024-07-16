types = []
changes = []
typemoney = int(input())

for i in range(typemoney):
    money = int(input())
    types.append(money)

amount = int(input())

types.sort(reverse = True)

for money in types:
    change = amount // money
    changes.append(change)
    amount = amount - change

print(types)
print(changes)