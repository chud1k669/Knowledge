import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))

s = {x for x in lst_in}

print(len(s))
#print(set(lst_in))