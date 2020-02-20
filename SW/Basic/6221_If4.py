li = ["가위", "바위", "보"]

m1 = input()
m2 = input()
winner = ""

if m1 == m2:
    print("Result : Draw")
else:
    if m1 == "가위":
        if m2 == "바위":
            winner = "Man2"
        elif m2 == "보":
            winner = "Man1"
    elif m1 == "바위":
        if m2 == "가위":
            winner = "Man1"
        elif m2 == "보":
            winner = "Man2"
    elif m1 == "보":
        if m2 == "바위":
            winner = "Man2"
        elif m2 == "가위":
            winner = "Man1"
    print("Result : %s Win!" % winner)