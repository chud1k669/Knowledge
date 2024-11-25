def is_triangle(a, b, c):
    return c < a + b

a, b, c = map(int, input().split())
print(is_triangle(a, b, c))