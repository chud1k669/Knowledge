s = input()
get_ra = lambda s: True if ("ra" in s) else False
print(get_ra(s))
# print((lambda s: True if ("ra" in s) else False )(s = input()))