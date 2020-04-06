import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 팰린드
# 발상 : 회문찾
# 변형 : 가로 세로 둘다 가능
# 조합 : 2차원 배열

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    flag, ans = False, ''

    # 가로
    for i in range(n):
        if flag:
            break
        for j in range(n-m+1):
            p = arr[i][j:j+m]
            for k in range(m//2):
                if p[k] != p[-(k+1)]:
                    break
                elif k == m//2 -1:
                    flag = True
                    ans = p

    # sol1 : 전치행렬 -> 가로 재탐색
    arr = [[x for x in row] for row in zip(*arr)]
    for i in range(n):
        if flag:
            break
        for j in range(n-m+1):
            p = ''.join(arr[i][j:j+m])  # 문자열 합쳐줘야 함
            for k in range(m//2):
                if p[k] != p[-(k+1)]:
                    break
                elif k == m // 2 - 1:
                    flag = True
                    ans = p

    print('#{} {}'.format(t, ans))
