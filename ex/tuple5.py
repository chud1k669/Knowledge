nums = list(map(int, input().split()))

unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

unique_nums_tuple = tuple(unique_nums)

print(*unique_nums_tuple)