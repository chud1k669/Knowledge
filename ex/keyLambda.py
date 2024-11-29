s = map(str, input().split())
sort_s = sorted(s, key = lambda i: -len(i))
print(*sort_s)