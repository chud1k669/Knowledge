parts = input().split()

d = {}

for i in range(1, len(parts)):
    d[i + 1] = parts[i]

print(d[4])