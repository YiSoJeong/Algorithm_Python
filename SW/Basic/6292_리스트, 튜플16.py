a = input()

print(list(map(int, a.split(', '))))
print(tuple(map(int, a.split(', '))))

# Why error? 뒤에 나오는 자료구조에 아무 항목이 들어가지 않음 ㅠ.
b = map(int, input().split(', '))

print(list(b))
print(tuple(b))
