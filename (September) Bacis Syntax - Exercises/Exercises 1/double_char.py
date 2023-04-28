while True:
    string = input()
    output = ""

    if string == "End":
        break
    else:
        for i in string:
            print(i * 2, end='')