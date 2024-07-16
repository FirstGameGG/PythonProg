def abecedarian(text):
    i = 0
    count = 1
    order = []
    for x in text:
        if i > 1:
            if text[i] > text[i - 1]:
                count += 1
            else:
                order.append(count)
                count = 0
        else:
            if i == 1 and text[i] > text[i - 1]:
                count += 2
        order.append(count)
        i += 1
    if len(order) > 0:    
        return max(order)
    else:
        return count

text = input().lower()
print(abecedarian(text))