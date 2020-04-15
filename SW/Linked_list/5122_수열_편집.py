import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : list
# 발상 : 수열에 숫자 삽입, 삭제, 교체 -> 리스트
# 변형 : 명령인자에 따라 연산 다르게 함
# 조합 : 가변인자 입력받기, 삼항연산자

T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    li = input().split()
    for _ in range(m):
        c, *a = input().split()  # 가변인자 입력받기
        if c == 'I':
            li.insert(int(a[0]), a[1])
        elif c == 'D':
            li.pop(int(a[0]))
        elif c == 'C':
            li[int(a[0])] = a[1]
    print('#{} {}'.format(t, -1 if l >= len(li) else li[l]))  # 삼항 연산자
