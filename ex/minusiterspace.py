string_fir_iter = input()     # Сохраняю пользовательские данные
it = iter(string_fir_iter)    # Создаю итератор
flag = True                   # Создаю флаг для условия цикла while
while flag:                   # Запускаем цикл
    simbol = next(it)         # Данные записываю в отдельную переменную
    if simbol != ' ':         # Если она не равна пробелу
        print(simbol, end="") # Выводим символ
    else:
        flag = False  