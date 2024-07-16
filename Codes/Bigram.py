def bigrams(text):
    bigrams = []
    for i in range(len(text)):
        if len(text[i: i+2]) == 2:
            bigrams.append(text[i: i+2])
    bigrams.sort()
    return bigrams
    
text = input('').lower()

for i in bigrams(text):
    print(i)
            
    