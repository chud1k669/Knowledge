m, n = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n == 1:
    print(f'{m-1:02}.{lst[m-2]} {m:02}.{n+1:02}')
elif n == lst[m-1]:
    print(f'{m:02}.{n-1:02} {m+1:02}.01')
else:
    print(f'{m:02}.{n-1:02} {m:02}.{n+1:02}')