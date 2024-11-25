def get_rect_value(length, width, tp=0):
    if tp == 0:
        return 2 * (length + width)  
    else:
        return length * width 
