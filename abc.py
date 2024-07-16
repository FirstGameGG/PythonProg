#Abecedarian
text = input()
count = 1
check = False 
i = 0

if len(text) == 0:
    count = 0
else:
    for ch in text:
        if i > 0:
            if ch.lower() > text[i-1].lower():
                count += 1
            else:
                break
        i += 1
print(count)