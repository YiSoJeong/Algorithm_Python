import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 구현
# 발상 : 주어진 영역만큼 색칠해보면서 판단해야 해서
# 변형 : 탐색하면서 색깔 겹치는 횟수 세기
# 조합 : 탐색

T = int(input())
for t in range(1, T+1):
    g = [[0]*10 for _ in range(10)]
    n = int(input())
    cnt = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if g[i][j] == 0:
                    g[i][j] = color
                elif g[i][j] != color:  # 한번 센 부분은 다음에 세지 X
                    cnt += 1
                    g[i][j] = -1
                elif g[i][j] < 0:
                    continue
    print('#{} {}'.format(t, cnt))
