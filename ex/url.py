import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


storage = {}

for input_value in lst_in:
    kush_check = input_value in storage

    if kush_check == True:
        print(f'Взято из кэша: HTML-страница для адреса {input_value}')

    if kush_check == False:
        print(f'HTML-страница для адреса {input_value}')
        storage[input_value] = input_value