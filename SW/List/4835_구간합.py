import sys
sys.stdin = open('../String/sample_input.txt', 'r')

# 분류 : Brute force
# 발상 : 이웃한 M개의 합 -> 다 해봐야 되는거 아닌가..ㅇㅅㅇ
# 변형 : 가장 큰 경우와 가장 작은 경우의 차
# 조합 : min, max -> sort 사용할 수도?

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    for i in range(n-m+1):
        res.append(sum(arr[i:i+m]))  # 배열을 계속 만들어서 시간초과 나면.. s, l로 인덱스 처리?
    res.sort()
    print('#{} {}'.format(t, res[n-m]-res[0]))
