n = int(input())
abs_gen = (abs(i) for i in range(-n, n+1))
cubes_gen = (i**3 for i in abs_gen)
first_four_values = [str(next(cubes_gen)) for _ in range(4)]

output = ' '.join(first_four_values)

print(output)