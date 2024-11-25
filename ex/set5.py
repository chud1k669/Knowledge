import sys 
lst_in = list(map(str.strip, sys.stdin.readlines()))

n = set()
for i in lst_in:
    n.add(i[0])

print(len(n))