word = input()
if word.lower() == word.lower()[::-1]:
    print('ДА')
else:
    print('НЕТ')