a = list(map(int, input().split()))
result = []
for i in a:
    result.extend([i, i])
print(*result)

