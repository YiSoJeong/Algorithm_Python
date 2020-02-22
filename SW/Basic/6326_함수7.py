a = int(input())


def factorial(a):
    ret = 1
    for i in range(2, a+1):
        ret *= i
    return ret


print(factorial(a))
