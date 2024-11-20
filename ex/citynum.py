list_1 = input().split()
listiks = [[list_1[i], int(list_1[i+1])] for i in range(0, len(list_1), 2)]
print(listiks)

