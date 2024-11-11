import math as m
n, k = map(int, input().split())
c = (m.factorial(n))/(m.factorial(k)*m.factorial(n-k))
print(int(c))