x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
fx = x
fy = y

xy = x * y
while True:
    if x % y == 0:
        gcd = y
        break
    else:
        gcd = x % y
        x = y
        y = gcd
        
lcm = int(xy / gcd)
print("  >> gcd({}, {}) ={:7}".format(fx, fy, gcd))
print("  >> lcm({}, {}) ={:7}".format(fx, fy, lcm))
    