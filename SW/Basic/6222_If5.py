a = input()

if 'A' <= a <= 'z':
    if 'A' <= a <= 'Z':
        print("%c(ASCII: %d) => %c(ASCII: %d)" % (ord(a), ord(a), ord(a)+32, ord(a)+32))
    else:
        print("%c(ASCII: %d) => %c(ASCII: %d)" % (ord(a), ord(a), ord(a)-32, ord(a)-32))
else:
    print(a)