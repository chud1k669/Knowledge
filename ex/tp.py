tp = input().strip()
if tp  == 'RECT':
    def get_sq(a, b = None):
        return a*b
elif tp != 'RECT':
    def get_sq(a, b = None):
        return a*a 