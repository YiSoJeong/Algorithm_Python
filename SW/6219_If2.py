a = int(input())
li = []

for i in range(1, a+1):
    if a % i == 0:
        if a//i > i:
            li.append(i)
            li.append(a // i)
        elif a//i == i:
            li.append(i)
        else: break

li.sort()

for x in li:
    print("%d(은)는 %d의 약수입니다." % (x, a))
if len(li) == 2:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (a, li[0], li[1]))
