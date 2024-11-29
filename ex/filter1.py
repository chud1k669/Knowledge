cities = map(str, input().split())
res = filter(lambda x: (len(x)>5), cities)
for _ in range(3):
    print(next(res), end=' ')
