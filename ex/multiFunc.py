def get_multi(digs):
    return min(digs) * max(digs)

digs = list(map(int, input().split()))
print(get_multi(digs))