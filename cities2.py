cities = ["Москва", "Тверь", "Вологда"]
a = list(map(str, input().split()))
lst = cities+a
print(*lst)