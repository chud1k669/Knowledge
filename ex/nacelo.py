n = int (input())
k = 0
for i in range (2 , n // 2 + 1):
    if n % i == 0:
        k = k + 1
if k <= 0:
    print('ДА')
else:
    print('НЕТ')