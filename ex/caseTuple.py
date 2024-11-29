t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [int(), str(), str()]:
        print("Yes")
    case [int(), str(), str(), float()]:
        print("Yes")
    case [int(), str(), str(), int()]:
        print("Yes")
    case [int(), str(), str(), float(), int()]:
        print("Yes")
    case _:
        print("No")