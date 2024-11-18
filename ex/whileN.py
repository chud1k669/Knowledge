n = int(input())
i = 1
if n >= 100:
        print('слишком большое значение n')
else:
    while i<= n:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=' ')
        i+=1