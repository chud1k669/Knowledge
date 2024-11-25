def rectangle(width, height):
    x = (width + height) * 2
    text = f"Периметр прямоугольника, равен {x}"
    print(text)

w, h = map(int, input().split())
rectangle(w, h)