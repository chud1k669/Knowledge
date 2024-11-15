cities = ["Москва", "Тверь", "Вологда"]
lst1 = list(map(str, input().split()))
lst = lst1+cities
print(*lst)