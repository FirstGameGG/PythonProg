text = "G2X3t4"
dig = ''
txt = ''
ls = []
for ch in text:
            if ch.isdigit():
                        checkdigit = True
                        checkstr = False
                        if checkdigit == True:
                                    dig += ch
                        else:
                                    ls.append(int(dig))
                                    dig = ''
            else:
                        checkstr = True
                        checkdigit = False
                        if checkstr == True:
                                    txt += ch
                        else:
                                    ls.append(txt)
                                    txt = ''

print(ls)
