def get_biggest_city(*args):
    word=""
    for city in args:
        if len(word) < len(city):
            word = city
    return word
