while True:
    try:
        a = input()
        if a == '':
            break
        else:
            print('>> {}'.format(a.upper()))
    except:
        break
