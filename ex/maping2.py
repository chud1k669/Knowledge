input_string = input()
lst = list(map(abs, map(int, input_string.split())))
print(*lst)