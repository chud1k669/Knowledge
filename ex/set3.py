n = input()
b = set()
for i in n:
    if i.isdigit():
        b.add(i)
if len(b) == 0:
    print("HEТ")
else:
    print(*sorted(b))