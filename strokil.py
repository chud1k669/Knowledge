m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

num = int(input())
m = list(map(str, m.split('\n')))
if num <= len(m):
    print(m[num-1])
else:
    print('IndexError')
