year = int(input())
v = 1000
i = 1
while i <= year:
    v = v*1.05
    i+=1
print(float(round(v, 2)))