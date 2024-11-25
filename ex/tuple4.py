names = input().lower().split()

filtered_names = [name for name in names if 'ва' in name]

tuple_names = tuple(filtered_names)

print(*tuple_names)