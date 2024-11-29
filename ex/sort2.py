def get_sort(d):
    return [value for key, value in sorted(d.items(), key=lambda item: item[0], reverse=True)]



d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}