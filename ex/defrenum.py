N = int(input())
def fib_rec(N, f=[1, 1]):
    if len(f) == N:
        print(f)
        return f
    next_fib = f[-1] + f[-2]
    f.append(next_fib)
    return fib_rec(N, f)
