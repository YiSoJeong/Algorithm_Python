import sys
sys.stdin = open('sample_input.txt', 'r')

# sol 1
# 분류 : Brute force
# 발상 : s2에 s1있는지 순서대로 비교
# 변형 : X
# 조합 : X

# T = int(input())
# for t in range(1, T+1):
#     ans = 0
#     s1 = input()
#     s2 = input()
#     for i in range(len(s2)-len(s1)+1):
#         if ans == 1:
#             break
#         for j in range(len(s1)):
#             if s2[i + j] != s1[j]:
#                 break
#             elif s2[i + j] == s1[j] and j == len(s1)-1:
#                 ans = 1
#
#     print('#{} {}'.format(t, ans))

# so1 2
# 분류 : KMP 알고리즘 (https://bowbowbow.tistory.com/6)
# 발상 : 문자열 비교 -> 패턴 매칭
# 변형 : X
# 조합 : X


# def get_pi(p):
#     m, j = len(p), 0
#     pi = [0]*m
#     for i in range(1, m):
#         while j > 0 and p[i] != p[j]:
#             j = pi[j-1]
#         if p[i] == p[j]:
#             j += 1
#             pi[i] = j
#     return pi
#
#
# def kmp(s, p):
#     pi, j = get_pi(p), 0
#     for i in range(len(s)):
#         while j > 0 and s[i] != p[j]:
#             j = pi[j-1]
#         if s[i] == p[j]:
#             if j == len(p)-1:
#                 return 1
#             else:
#                 j += 1
#     return 0
#
#
# T = int(input())
# for t in range(1, T+1):
#     s1 = input()
#     s2 = input()
#
#     print('#{} {}'.format(t, kmp(s2, s1)))

# so1 3
# 분류 : Boyer Moore 알고리즘 (https://xenostudy.tistory.com/72, https://tae-ho.tistory.com/12?category=696576)
# 발상 : 문자열 비교 -> 패턴 매칭
# 변형 : X
# 조합 : X


