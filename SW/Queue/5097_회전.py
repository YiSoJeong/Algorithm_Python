import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 큐 (mod 연산)
# 발상 : deQueue -> enQueue 반복
# 변형 : 맨 앞의 숫자를 맨 뒤로 보내기
# 조합 : mod 연산, 원형 리스트(큐)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(t, arr[M % N]))
