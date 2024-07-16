text = input()
step = int(input())

if abs(step) > len(text) and len(text) > 0:
        step %= len(text)

print(text[-step:] + text[:-step])