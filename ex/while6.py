n,m = map(int, input().split())

while n <= m:
    if n%2==1:
        print(n, end=' ')
        n+=1
    else:
        n+=1