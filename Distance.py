import math

while True:
    print('<<Point a>>')
    xa = int(input('Enter x coordinate: '))
    ya = int(input('Enter y coordinate: '))
    print('<<Point b>>')
    xb = int(input('Enter x coordinate: '))
    yb = int(input('Enter y coordinate: '))    
    
    
    if xa == 0 and xb == 0 and ya == 0 and yb == 0:
        break
    
    print('Distance between (%d, %d) and (%d, %d):'%(xa, ya ,xb, yb))
    
    euclid = math.sqrt((xa - xb)**2 + (ya - yb)**2)
    horizon = abs(xa - xb)
    vertical = abs(ya - yb)
    
    print('Euclidean distance is %.2f.' %(euclid))
    print('Horizontal distance is %d.' %(horizon))
    print('Vertical distance is %d.' %(vertical))
    
    if xb - xa == 0 and yb - ya == 0:
        print('We are going nowhere.')
    elif xb - xa == 0 and yb - ya > 0:
        print('We are going north.')
    elif xb - xa == 0 and yb - ya < 0:
        print('We are going south.')
    elif xb - xa < 0 and yb - ya == 0:
        print('We are going west.')
    elif xb - xa > 0 and yb - ya == 0:
        print('We are going east.') 
        
    elif xb - xa < 0 and yb - ya > 0:
        print('We are going north-west.')
    elif xb - xa < 0 and yb - ya < 0:
        print('We are going south-west.')
    elif xb - xa > 0 and yb - ya > 0:
        print('We are going north-east.')
    elif xb - xa > 0 and yb - ya < 0:
        print('We are going south-east.')
        
print('Goodbye')