import math

input_str = input()
numbers = list(map(int, input_str.split()))
n = int(math.sqrt(len(numbers)))
lst = [numbers[i:i+n] for i in range(0, len(numbers), n)]
for row in lst:
    print(*row)
