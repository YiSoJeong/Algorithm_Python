import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Brute Force
# 발상 : 문자열에 있는 알파벳 개수 구한 후 패턴에 있는 문자들 추출
# 변형 : 패턴에 포함되어 있는 글자들이 문자열에 몇 개씩 있는지 찾아라
# 조합 : 아스키 코드 변환 A:65 a:97 알파벳 수:26

T = int(input())
for t in range(1, T+1):
    alphabet = {chr(i): 0 for i in range(65, 91)}
    ans = 0
    s1, s2 = input(), input()
    for x in s2:
        alphabet[x] += 1
    for x in s1:
        if ans < alphabet[x]:
            ans = alphabet[x]
    print('#{} {}'.format(t, ans))
