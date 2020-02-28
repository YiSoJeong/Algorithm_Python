a = input()
flag = True

for i in range(len(a)//2):
    if a[i] != a[-(i + 1)]:
        flag = False
        break

print(a)
if flag:
    print('입력하신 단어는 회문(Palindrome)입니다.')
