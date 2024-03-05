#Bad Genius
def correction(text):
    new = ''
    for ch in text:
        if ch != ' ':
            if ch not in new:
                new += ch
    return new
message = input()
password = input()
encrypt = input()

message = correction(message)
password = correction(password)

for ch in encrypt:
    if ch in password:
        indexmess = password.find(ch)
        print(message[indexmess])