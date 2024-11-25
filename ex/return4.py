def unname(word):
    return False if len(word) < 6 else True


cities = input().split()
lst = [i for i in cities if unname(i)]
print(*lst)