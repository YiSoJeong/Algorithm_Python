import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Greedy
# 발상 : BabyGin -> 기본적인 Greedy 문제 cf. 배열이 두 개(player1, player2)라 완전탐색은 조금 빡셀수도..
# 변형 : 두 선수가 번갈아 가며 카드를 뽑고 BabyGin이 먼저 나오는 선수가 승자
# 조합 :


def baby_gin(arr, idx):
    if arr[idx] == 3:
        return True
    if 0 <= idx <= 7 and arr[idx] >= 1 and arr[idx+1] >= 1 and arr[idx+2] >= 1:
        return True
    if 1 <= idx <= 8 and arr[idx-1] >= 1 and arr[idx] >= 1 and arr[idx+1] >= 1:
        return True
    if 2 <= idx <= 9 and arr[idx] >= 1 and arr[idx-1] >= 1 and arr[idx-2] >= 1:
        return True
    return False


T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0]*10
    player2 = [0]*10
    winner = 0
    for i in range(0, 12, 2):
        player1[cards[i]] += 1
        if baby_gin(player1, cards[i]):
            winner = 1
            break
        player2[cards[i+1]] += 1
        if baby_gin(player2, cards[i+1]):
            winner = 2
            break

    print('#{} {}'.format(t, winner))
