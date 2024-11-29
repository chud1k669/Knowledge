nums = list(map(float, input().split()))
result = (any(num < 0 for num in nums))
print(result)