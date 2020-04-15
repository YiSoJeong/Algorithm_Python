import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : list
# 발상 : 제공된 숫자에 추가하면서 비밀번호 찾음 -> list 원소 삽입
# 변형 : list 중간에 원소 삽입 반복
# 조합 : 구현, 리스트 슬라이싱

T = int(input())
for t in range(1, T+1):
    n, m, k = map(int, input().split())
    li = list(map(int, input().split()))
    i, l = m, n
    for _ in range(k):
        if i == l:
            li.insert(i, li[i-1]+li[0])
        else:
            if i > l:
                i = i-l  # 앞으로 돌아옴
            li.insert(i, li[i-1]+li[i])
        l += 1  # 길이 갱신
        i += m  # 인덱스 이동
    print('#{} {}'.format(t, ' '.join(map(str, li[-1:-11:-1]))))
