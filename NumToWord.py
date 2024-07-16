adict = {'00':'','01':'one','02':'two','03':'three','04':'four','05':'five','06':'six','07':'seven','08':'eight','09':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}

bdict = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

cdict = {'0':'','1':'one','2':'twen','3':'thir','4':'for','5':'fif','6':'six','7':'seven','8':'eigh','9':'nine'}
num = input()
if num.isnumeric():
    if int(num) > 999 or int(num) < 0:
        print('ERROR')
    else:
        num = str(int(num))
        if len(num) == 3:
            print(bdict[num[0]],end = '')
            print('-hundred', end = '')
            if num[1:] in adict:
                if num[1:] != '00':
                    print("-", end ='')
                print(f"{adict[num[1:]]}",end = '')
            else:
                print(f"-{cdict[num[1]]}ty", end = '')
                if num[2] != '0':
                    print(f"-{bdict[num[2]]}")
        elif len(num) == 2:
            if num[0:] in adict:
                print(adict[num[0:]],end = '')
            else:
                print(f"{cdict[num[0]]}ty", end = '')
                if num[1] != '0':
                    print(f"-{bdict[num[1]]}")
        else:
            print(bdict[num[0]],end = '')
else:
    print('ERROR')