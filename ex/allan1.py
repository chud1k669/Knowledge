nums = list(map(int, input().split()))
result = (all(num % 2 == 0 for num in nums))
print(result)