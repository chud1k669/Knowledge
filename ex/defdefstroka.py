def get_div(div):
    def get_stroka(stroka):
        return f'<{div}>{stroka}</{div}>'
    return get_stroka(stroka)

div = input()
stroka = input()
print(get_div(div))