numbers = input()
digits = list(map(int, numbers))
if sum(digits[:3]) == sum(digits[3:]):
    print('ДА')
else:
    print('НЕТ')