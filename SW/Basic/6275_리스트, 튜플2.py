string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
rem = ['a', 'e', 'i', 'o', 'u']

ret = [x for x in string if x not in rem]
for s in ret:
    print(s, end='')
