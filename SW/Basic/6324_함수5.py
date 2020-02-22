li = [1, 2, 3, 4, 3, 2, 1]


def remove_dup(arr):
    ret = []
    for x in arr:
        if x not in ret:
            ret.append(x)
    print(ret)


print(li)
remove_dup(li)