# a, b, c, d = map(int,input().split())

# if b > a:
#     a,b = b,a
# if d > c:
#     c,d = d,c
#     (a - c > 2 and b - d > 2)
#     print('ДА')

# else:
#      print('ДА')
# Чтение четырех чисел из ввода
a, b, c, d = map(int, input().split())

# Вычисляем минимальные допустимые размеры конверта с учетом зазоров
min_a = a - 2
min_b = b - 2

# Проверяем, помещается ли открытка в конверт в обеих ориентациях
if (c <= min_a and d <= min_b) or (c <= min_b and d <= min_a):
    print("ДА")
else:
    print("НЕТ")