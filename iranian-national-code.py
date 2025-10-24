data = input("enter your national code: ")
if len(data) != 10:
    print("not valid!")
else:
    kol = int(data[0])*10 + int(data[1])*9 + int(data[2])*8 + int(data[3])*7 + int(data[4])*6 + int(data[5])*5 + int(data[6])*4 + int(data[7])*3 + int(data[8])*2
    total = kol % 11
    if total < 2:
        if int(data[9]) == total:
            print("you're iranian")
        else:
            print("you're not iranian")
    else:
        if int(data[9]) == (11 - total):
            print("you're iranian")
        else:
            print("you're not iranian")