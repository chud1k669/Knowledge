cities_string = input().strip()

cities = cities_string.split()


result = "ДА"

for i in range(1, len(cities)):
    prev_city = cities[i - 1]
    curr_city = cities[i]

    last_char = prev_city[-1]
    

    if last_char in ['ь', 'ъ', 'ы']:
        last_char = prev_city[-2]

    if last_char.lower() != curr_city[0].lower():
        result = "НЕТ"
        break

print(result)