import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Linked List
# 발상 : 배열에 삽입이 많음 -> 링크드 리스트
# 변형 : 수열의 인덱스에 숫자 추가
# 조합 :

# sol1 : list의 insert함수를 이용해서 쉽게 추가 but 느림
T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    li = list(input().split())

    for _ in range(m):
        idx, val = map(int, input().split())
        li.insert(idx, val)

    print('#{} {}'.format(t, li[l]))

# sol2 : linked list로 원소 추가
# https://www.fun-coding.org/DS&AL1-4.html : 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원한다고 함;
