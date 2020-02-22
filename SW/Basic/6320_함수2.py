def winner(a, b):
    win = ''
    if a == b:
        return win
    else:
        if a == '가위':
            if b == '바위':
                win = '바위'
            elif b == '':
                win = '가위'
        elif a == '바위':
            if b == '가위':
                win = '바위'
            elif b == '보':
                win = '보'
        elif a == '보':
            if b == '바위':
                win = '보'
            elif b == '가위':
                win = '가위'
        return win


p1 = input()
p2 = input()

print("{}가 이겼습니다!".format(winner(input(),input())))
