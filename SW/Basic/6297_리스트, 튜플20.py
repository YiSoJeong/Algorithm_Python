a = list(map(int, input().split(', ')))
result = [x for x in a if x % 2 == 1]

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(result[i], end=', ')
