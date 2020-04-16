import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Stack
# 발상 : 괄호의 짝 검사 -> 스택으로 관리 ( 를 넣어놓고 ) 만나면 pop
# 변형 : 여러 모양의 괄호 존재
# 조합 :

T = int(input())
for t in range(1, T+1):
    s = input()
    stack = []
    ans = 1
    for x in s:
        if x == '(' or x == '{':
            stack.append(x)
        elif x == ')' or x == '}':
            if not stack:
                stack = [x]
                break
            else:
                if (x == ')' and stack[-1] == '(') or (x == '}' and stack[-1] == '{'):
                    stack.pop()
                else:  # 짝 안맞음
                    stack = [x]
                    break
    if stack:
        ans = 0
    print('#{} {}'.format(t, ans))
