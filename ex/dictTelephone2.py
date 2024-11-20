import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for item in lst_in:
    phone, name = item.split(maxsplit=1)
    d.setdefault(name, []).append(phone)

sorted_items = sorted(d.items())
for key, value in sorted_items:
    print(f"({key}, {value})")