def get_str(str1, tag="DIV", up=True):
    if up == True:
        return f'<{tag}>{str1}</{tag}>'
    else:
        return f'<{tag}>{str1}</{tag}>'

a = input()
print(get_str(a))
print(get_str(a, tag="div", up=False))