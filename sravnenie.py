numbers = list(map(int, input().split()))
if numbers[0] < numbers[1] and numbers[0] < numbers[2]:
    print(numbers[0])
elif numbers[1] < numbers[0] and numbers[1] < numbers[2]:
    print(numbers[1])
elif numbers[2] < numbers[0] and numbers[2] < numbers[1]:
    print(numbers[2])
else:
    print(numbers[1])