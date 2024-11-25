import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
unique_guests = set(lst_in)

print(len(unique_guests))