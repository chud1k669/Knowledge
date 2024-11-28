def get_str(stroka):
    tagstart = "<h1>"
    tagend = "</h1>"
    def in_def():
        return f'{tagstart}{stroka}{tagend}'
    return in_def()

print(get_str(input()))