import sys

# Чтение входных данных
lst_in = list(map(str.strip, sys.stdin.readlines()))

tuples = tuple(tuple(item.split('=')) for item in lst_in)
filtered_tuples = tuple(filter(lambda t: int(t[1]) >= 500, tuples))
names = [t[0] for t in filtered_tuples]
print(' '.join(names))