fib = [1, 1]
fib.extend(fib[x-1] + fib[x] for x in range(1, 9))

print(fib)
