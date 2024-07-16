homework = int(input(""))
quiz = int(input(""))
test = int(input(""))

total = homework + quiz + test

if homework < 0 or quiz < 0 or test < 0:
    print("Error")
elif homework > 20 or quiz > 20 or test > 60:
    print("Error")
else:
    if total >= 80:
        print("A")
    elif total >= 75:
        print("B+")
    elif total >= 70:
        print("B-")
    elif total >= 65:
        print("C+")
    elif total >= 60:
        print("C-")
    elif total >= 55:
        print("D+")
    elif total >= 50:
        print("D-")
    else:
        print("F")