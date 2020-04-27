import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Greedy
# 발상 : 도크의 사용횟수 최대 -> 회의실 배정 문제와 비슷(탐욕 알고리즘 대표문제)
# 변형 : 최대 도크 사용 가능 횟수 구하기
# 조합 : sort(key=lamba x: x[1]) 정렬 내장함수
# https://www.notion.so/ssospace/Python-10cc0bee505e4478be3440ba527e9a33 정렬
# https://www.notion.so/ssospace/7-9816f546ed684109a9beefb698eed0e3 람다식

T = int(input())
for t in range(1, T+1):
    N = int(input())
    blocks = []
    ans = 0
    for _ in range(N):
        item = list(map(int, input().split()))
        blocks.append(item)
    blocks.sort(key=lambda x: x[1])
    end = 0
    for block in blocks:
        if block[0] >= end:
            ans += 1
            end = block[1]
    print('#{} {}'.format(t, ans))
