n, m = map(int, input().split())
c = n+m
if c%20!=0:
    print((c//20)+1)
else:
    print(c//20)