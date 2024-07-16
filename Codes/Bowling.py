frame = 1
point = 0
while frame <= 10:
    print("Frame # {}".format(frame))
    down = int(input("  Number of pins down: "))
    if down == 10:
        point += 10
    else:
        print("Frame # {}".format(frame))
        redown = int(input("  Number of pins down (0-{}): ".format(10 - down)))
        point += redown + down
    frame += 1
    
print("Total score is %d" %(point))
        
        
        
    