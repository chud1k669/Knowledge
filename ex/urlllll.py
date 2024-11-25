import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = ()
for i in range(len(lst_in)):
    t = tuple(lst_in[i].split())
    menu += (t,)
print(menu)