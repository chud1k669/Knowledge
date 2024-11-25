import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


d = {}

for entry in lst_in:
    author, title = entry.split(':')
    author = author.strip()
    title = title.strip()
    

    if author in d:
        d[author].add(title)
    else:
        d[author] = {title}
