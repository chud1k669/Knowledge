months = '''31 28 31 30 31 30 31 31 30 31 30 31'''

num = int(input())
months = list(map(str, months.split(' ')))
if num <= len(months):
    print(months[num-1])
else:
    print('Error!')