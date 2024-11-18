res = []
while len(res) < 6:
    n = input()
    res.append(n)

i=0
while i<len(res):
    if ' ' in res[i]:
        res.pop(i)
    else:
        i+=1
print(*res)