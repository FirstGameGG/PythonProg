notes = input()
step = int(input())
ls = notes.split(',')
ls.pop()
if step > len(ls):
    step %= len(ls)
print(ls[step - 1])