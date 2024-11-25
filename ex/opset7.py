n = int(input())
div_1 = {2, 3, 5}
result = set()
for i in div_1:
    if n % i == 0:
        result.add(i)


print('ДА' if result == {2, 3, 5} else 'НЕТ')