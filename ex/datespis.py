import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
birthday_dict = {}

for line in lst_in:
    parts = line.split(maxsplit=1)
    day = int(parts[0])  # День рождения
    name = parts[1].strip()  # Имя человека
    

    if day not in birthday_dict:
        birthday_dict[day] = [name]
    else:
        birthday_dict[day].append(name)

for day, names in sorted(birthday_dict.items()):
    print(f"{day}: {', '.join(names)}")