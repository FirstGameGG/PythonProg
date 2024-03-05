def decode_lucas(text):
    vowels = 'aeiou'
    new_text = ""
    skip = 0

    for i in range(len(text)):
        if skip:
            skip -= 1
            continue
        if text[i] in vowels and i+2 < len(text) and text[i+1] == 'p' and text[i+2] == text[i]:
            new_text += text[i]
            skip = 2
        else:
            new_text += text[i]

    return new_text

text = input('')
print(decode_lucas(text))
