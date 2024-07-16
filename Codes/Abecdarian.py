text = input()

if len(text) == 0:
    order = 0
else:
    count = 1
    maxchr = text[0]
    i = 0
    order = 0
    for ch in text:
        if i > 0:
            if ch > maxchr:
                count += 1
                maxchr = ch
            else:
                if count >= order:
                    order = count
                count = 0
                maxchr = ch
            i += 1

print(order)