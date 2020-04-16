import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : DP
# 발상 : 일정한 모양의 종이가 반복되면서 늘어남 -> 규칙(점화식)이 있지 않을까..
# 변형 : 직사각형에 종이를 빈틈없이 붙이기
# 조합 :

T = int(input())
for t in range(1, T+1):
    dp = [0]*31
    dp[1] = 1
    dp[2] = 3
    n = int(input())//10
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    print('#{} {}'.format(t, dp[n]))
