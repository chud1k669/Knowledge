def get_add(a, b):
    if type(a) != bool != type(b):
        if isinstance(a, (int, float)) == isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) == isinstance(b, str):
            return a + b