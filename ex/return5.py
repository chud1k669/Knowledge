def get_string_and_length(s):
    return s, len(s)

cities_str = input().strip()

cities = cities_str.split()

d = {city: length for city, length in map(get_string_and_length, cities)}
a = sorted(d, key=d.get)
print(*a)