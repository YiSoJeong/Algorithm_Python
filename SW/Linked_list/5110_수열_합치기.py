import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 리스트
# 발상 : 수열 -> 리스트
# 변형 : 수열의 첫 번째 원소의 크기에 따라 기존의 수열에 추가
# 조합 : 정렬, 리스트 조작, 리스트 슬라이싱
# 리스트 조작 : https://dojang.io/mod/page/view.php?id=2281
# 리스트 슬라이싱 : https://dojang.io/mod/page/view.php?id=2208

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    for _ in range(n-1):
        tmp = list(map(int, input().split()))
        for i in range(len(li)):
            if tmp[0] < li[i]:
                li[i:i] = tmp  # 리스트에 리스트 추가하기(원소만)
                break
            elif i == len(li)-1 and tmp[0] > li[i]:
                li.extend(tmp)
    print('#{} {}'.format(t, ' '.join(map(str, li[-1:-11:-1]))))  # 리스트 역순으로 출력하기