num1, num2 = map(int, input().split())
if num1 % num2 == 0:
    print(num1//num2)
else:
    print(f'{num1} на {num2} нацело не делится')