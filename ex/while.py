n,m = list(map(int, input().split()))
lst=[]
while n <= m:
    i = n**2
    n+=1
    lst.append(i)
print(*lst)   