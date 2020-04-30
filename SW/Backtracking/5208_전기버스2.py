import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Backtracking
# 발상 : 갈 수 있는 데 까지 가보고 최소 cnt가 아니면 전 정류장에서 충전하고의 반복 -> 백트래킹
# 변형 : 전기버스가 목적지에 도착하는데 필요한 배터리 최소 교환 횟수
# 조합 : dfs, recursion


def dfs(cur):
    global cnt, ans

    if cnt > ans:
        return

    if cur >= N:  # 도착지점을 넘으면 종료
        if cnt < ans:
            ans = cnt
        return

    for i in range(cur + arr[cur], cur, -1):  # 이 반복문을 생각 해내는게 너무 어려웠음 ㅠ
        cnt += 1
        dfs(i)
        cnt -= 1


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    cnt, ans = -1, float('inf')  # 처음 충전은 제외 : 사소하지만 중요했던 처리..!
    dfs(1)
    print('#{} {}'.format(t, ans))
