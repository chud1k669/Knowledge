a = map(int, input().split())
b = map(int, input().split())
c = (i*j for i, j in zip(a,b))
[print(next(c), end=' ')for _ in range(3)]