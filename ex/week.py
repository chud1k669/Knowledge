m = '''понедельник
вторник
среда
четверг
пятница
суббота
воскресенье'''

num = int(input())
m = list(map(str, m.split('\n')))
if num <= len(m):
    print(m[num-1])
else:
    print('IndexError')
