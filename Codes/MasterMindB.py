text1 = input()
text2 = input()
countsameloc = 0
countsamechr = 0
text1 = [ch.lower() for ch in text1]
text2 = [ch.lower() for ch in text2]
i = 0
while i < len(text1):
    if text1[i] == text2[i]:
        text1.pop(i)
        text2.pop(i)
        countsameloc += 1
        continue
    i += 1
    
for ch2 in text2[:]:
    if ch2 in text1:
        text1.remove(ch2)
        countsamechr += 1

print(f"{countsameloc}-{countsamechr}")
