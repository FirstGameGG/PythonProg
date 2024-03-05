cordinate = []

h , w = input().split('x')

#table create
ls = list(range(int(h)))
for i in ls:
    ls[i] = [0] * int(w)

bombamount = int(input())

# loop bomb input and add
for i in range(bombamount):
    x , y =  input().split(',')
    bomb = int(x) , int(y)
    cordinate.append(bomb)

#add bomb
for x , y in cordinate:
    if x < int(w) and y < int(h):  # Ensure coordinates are within table dimensions
        ls[y][x] = '*'
    else:
        print(f"Bomb coordinates ({x}, {y}) exceed table dimensions.")

#print table
for i in ls:
    print(i)
