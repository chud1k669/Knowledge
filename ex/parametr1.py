def func_show(func):
    def wrapper(*args):
        print ( "Площадь прямоугольника:", func(*args))
    return wrapper

@func_show
def get_sq(width,height):
    return width * height