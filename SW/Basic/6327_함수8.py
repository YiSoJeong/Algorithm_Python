arr = list(map(int, input().split(sep=',')))


def square(a):
    return a*a


for x in arr:
    print("square({}) => {}".format(x, square(x)))