li = [2, 4, 6, 8, 10]


def find_el(a, arr):
    if a in arr:
        print("{} => True".format(a))
    else:
        print("{} => False".format(a))


print(li)
find_el(5, li)
find_el(10, li)
