def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

s=[int(i) for i in input().split()]
lst=filter_lst(s,lambda a:a)
print(*lst)
lst=filter_lst(s,lambda a: a < 0)
print(*lst)
lst=filter_lst(s,lambda a: a >= 0)
print(*lst)
lst=filter_lst(s,lambda a: a >= 3 and a <= 5)
print(*lst)