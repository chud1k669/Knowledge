city = list(map(str, input().split()))

if "Ульяновск" in city:
    city.remove("Ульяновск")
    
new_tuple = tuple(city)

print(*new_tuple)