import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Backtracking
# 발상 : 2차원 배열에서 한 열에 하나씩 선택하며 최솟값 -> N-Queen(백트래킹)
# 변형 : N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산할 때의 최소비용
# 조합 : DFS, Recursion


def dfs(y):
    global ans, total
    if ans < total:  # 끝까지 안가도 최솟값보다 크면 탈락
        return

    if y == N:
        if total < ans:
            ans = total
        return          # 끝까지 가면 return 은 무조건 해줌

    for i in range(N):
        if not visit[i]:
            total += arr[y][i]
            visit[i] = True
            dfs(y+1)
            visit[i] = False
            total -= arr[y][i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    ans, total = float('inf'), 0  # 초기값을 최대로 설정
    dfs(0)
    print('#{} {}'.format(t, ans))
