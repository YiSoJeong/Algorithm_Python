a = int(input())
bi = []

while a != 0:
    bi.append(a % 2)
    a //= 2

while len(bi):
    print(bi.pop(0), end="")
