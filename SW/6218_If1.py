a = int(input())
s = set()

for i in range(1, a+1):
    if a % i == 0:
        s.add(i)
        s.add(a//i)
        if a//i <= i:
            break

for x in sorted(s):
    print("%d(은)는 %d의 약수입니다." % (x, a))
