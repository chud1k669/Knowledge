city = input()
n = set()

while city != "q":
    n.add(city)
    city = input()
print(len(n))