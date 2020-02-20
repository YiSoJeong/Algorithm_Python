a = input()
num = [0]*10

for x in a:
    num[int(x)] += 1

print("0 1 2 3 4 5 6 7 8 9")
for i in range(len(num)):
    if i == len(num) - 1:
        print(num[i])
    else: print(num[i], end=' ')
