s =input()
c = 1
i=0
while i <= c:
    c = s.count('-')
    i+=1
    s = s.replace('--', '-')
print(s)