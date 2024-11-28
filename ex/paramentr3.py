def sort_decorator(func):
    def wrapper(s):
        lst = func(s)
      
        lst.sort()
        
        return lst
    return wrapper

@sort_decorator
def get_list(s):
    return list(map(int, s.split()))

input_string = input()
sorted_lst = get_list(input_string)
print(*sorted_lst)