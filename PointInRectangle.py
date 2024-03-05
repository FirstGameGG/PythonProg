print('Upper left corner coordinate:')

x = int(input('  << x axis: '))
y = int(input('  << y axis: '))
east = int(input('  << Eastern: '))
south = int(input('  << Southern: '))

print('Enter a coordinate:')
xa = int(input('  << x axis: '))
ya = int(input('  << y axis: '))

if xa < x or xa > (x + east):
    x_rectangle = False
else:
    x_rectangle = True
    
if ya > y or ya < (y - south):
    y_rectangle = False
else:
    y_rectangle = True    
    
if x_rectangle == True and y_rectangle == True:
    print('>>> (%.2f, %.2f) is inside the rectangle.'%(xa , ya))
else:
    print('>>> (%.2f, %.2f) is not inside the rectangle.'%(xa , ya))
    