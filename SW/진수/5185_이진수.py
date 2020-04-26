import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 진수 변환
# 발상 : 16진수 -> 2진수
# 변형 :
# 조합 : x진수 -> 10진수 : int(num, base=) https://programmers.co.kr/learn/courses/4008/lessons/12733
#       10진수 -> 2, 8, 16진수 : bin(), oct(), hex()

T = int(input())
for t in range(1, T+1):
    N, a = input().split()
    res = bin(int(a, base=16))
    base_len = 4*int(N)
    res = '0'*(base_len-len(res[2:]))+res[2:]
    print('#{} {}'.format(t, res))
