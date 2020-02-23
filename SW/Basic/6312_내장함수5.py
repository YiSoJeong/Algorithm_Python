def multiple(*params):
    ret = 1
    for x in params:
        if type(x) != int:
            ret = '에러발생'
            break
        else:
            ret *= x
    return ret


print(multiple(1, 2, '4', 3))
