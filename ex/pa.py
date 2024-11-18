str1 = input()

if not 'ра' in str1: 
    print(-1)
else:
    for i, v in enumerate(str1[:-1]):
        if v == 'р' and str1[i+1] == 'а':
            print(i, end= ' ')
            
        