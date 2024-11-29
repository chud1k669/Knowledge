N = int(input())

def get_sum(total):
    current_sum = 0
    for number in range(1, total + 1):
        current_sum += number
        yield current_sum
