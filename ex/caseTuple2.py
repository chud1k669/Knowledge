t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [int(), author, title] if len(author) >= 6 and len(title) >= 10:
        print("Yes")
    case [int(), author, title, price] if len(author) >= 6 and price > 0:
        print("Yes")
    case [int(), author, title, year] if len(author) >= 6 and year >= 2020:
        print("Yes")
    case [int(), author, title, price, year] if len(author) >= 6 and price > 0 and year >= 2020:
        print("Yes")
    case _:
        print("No")