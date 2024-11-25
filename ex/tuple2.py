city = tuple(map(str, input().split()))
if "Москва" not in city:
    new_tuple = city + ("Москва",)
print(*new_tuple)