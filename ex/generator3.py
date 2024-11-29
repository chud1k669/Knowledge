a,b = map(int, input().split())
gen = (abs(i) for i in range(a, b) )
for _ in range(5):
    print(next(gen))