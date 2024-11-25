
def check_password(password, chars="$%!?@#"):

    has_special_char = any(char in password for char in chars)
    
    min_length = len(password) >= 8

    return has_special_char and min_length
