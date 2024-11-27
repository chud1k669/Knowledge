def get_str(str1, tag="h1"):
    return f'<{tag}>{str1}</{tag}>'

a = input()
print(get_str(a))
print(get_str(a, tag="div"))