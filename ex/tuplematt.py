a = int(input())
k = []
for i in range(a):
    k.append([0] * a)
for i in range(a):
    for j in range(a):  # цыкл для обработки
        if i == j:
            k[i][j] = 1
        print(k[i][j], end=' ', sep = '')
    print('\r')