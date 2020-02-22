a = int(input())


def fib(n):
    arr = [1]*n
    for x in range(2, n):
        arr[x] = arr[x-2] + arr[x-1]
    return arr


print(fib(a))
