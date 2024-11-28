menu = input() 
def show_menu(func):
    def wrapper(s):
        menu_list = func(s)
        for index, item in enumerate(menu_list, start=1):
            print(f"{index}. {item}")
        return menu_list
    return wrapper

@show_menu
def get_menu(s):
    return s.split()