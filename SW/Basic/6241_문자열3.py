a = input()

protocol = a.find(':')
host1 = a.find('//')
host2 = a.find('/', host1 + 2)
others = a.rfind('/')

print('''protocol: {}
host: {}
others: {}'''.format(a[0:protocol], a[host1+2: host2], a[others + 1:]))
