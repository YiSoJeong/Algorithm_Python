import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Stack
# 발상 : 스택에 들어갈 원소가 top이랑 같으면 pop시켜주면서 중복 제거
# 변형 : 문자열에서 반복문자 지우기
# 조합 : 문자열

T = int(input())
for t in range(1, T+1):
    string = input()
    stack = []
    for x in string:
        if not len(stack):
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    print('#{} {}'.format(t, len(stack)))
