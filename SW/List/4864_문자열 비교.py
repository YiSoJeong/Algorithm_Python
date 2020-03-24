import sys
sys.stdin = open('sample_input.txt', 'r')

# sol 1
# 분류 : Brute force
# 발상 : s2에 s1있는지 순서대로 비교
# 변형 : X
# 조합 : X

T = int(input())
for t in range(1, T+1):
    ans = 0
    s1 = input()
    s2 = input()
    for i in range(len(s2)-len(s1)+1):
        if ans == 1:
            break
        for j in range(len(s1)):
            if s2[i + j] != s1[j]:
                break
            elif s2[i + j] == s1[j] and j == len(s1)-1:
                ans = 1

    print('#{} {}'.format(t, ans))
