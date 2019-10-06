L, A, B, C, D = [int(input()) for _ in range(5)]

if B % D:
    math = B // D + 1
else:
    math = B // D

if A % C:
    kor = A // C + 1
else:
    kor = A // C

print(L - max(math, kor))
