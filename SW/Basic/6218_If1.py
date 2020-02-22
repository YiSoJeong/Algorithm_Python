n = int(input())

# 1 : N = a * b 일 때, a <= b를 만족할 때 까지만 반복하기
def divisor_my(a):
    s = set()
    for i in range(1, a+1):
        if a % i == 0:
            s.add(i)
            s.add(a//i)
            if a//i <= i:
                break
    for x in sorted(s):
        print("%d(은)는 %d의 약수입니다." % (x, a))


# 2 : N = a * b 일 때, a의 최소이자 b의 최대가 되는 수는 N ** 0.5 활용하기
def divisor_root(a):
    s = set()
    for i in range(1, round(a ** 0.5)+1):
        if a % i == 0:
            s.add(i)
            s.add(a//i)
    for x in sorted(s):
        print("%d(은)는 %d의 약수입니다." % (x, a))


divisor_my(n)
print()
divisor_root(n)