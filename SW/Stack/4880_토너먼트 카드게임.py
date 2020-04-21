import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 분할정복
# 발상 : 그룹을 두 개로 나누면서 해를 구함
# 변형 : 토너먼트 형식의 카드게임
# 조합 : dfs, 재귀, 백트래킹


def win(first, second):
    # 비김 번호 작은 순
    if a[first-1] == a[second-1]:
        return first
    # 가위로 이김
    elif a[first-1] == 1 and a[second-1] == 3:
        return first
    # 바위로 이김
    elif a[first-1] == 2 and a[second-1] == 1:
        return first
    # 보로 이김
    elif a[first-1] == 3 and a[second-1] == 2:
        return first
    return second


# 두 그룹에서의 승자를 재귀로 반복 구함
# 두 명이 될 때까지 나누고 승자를 차례로 반환
def match(start, end):
    # 한 명일 때는 자기 번호 반환
    if start == end:
        return start

    first_winner = match(start, (start+end)//2)
    second_winner = match((start+end)//2+1, end)
    return win(first_winner, second_winner)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    print('#{} {}'.format(t, match(1, N)))
