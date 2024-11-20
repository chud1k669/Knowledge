list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
ressult = [n + m for i, n in enumerate(list_1) for j, m in enumerate(list_2) if i == j]
print(ressult)

#print(*[int(n) + int(m) for i, n in enumerate(input().split()) for j, m in enumerate(input().split()) if i == j])
