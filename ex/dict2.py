d = dict([x.split('=') for x in input().split()])
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))