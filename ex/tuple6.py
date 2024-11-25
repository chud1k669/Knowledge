nums = list(map(int, input().split()))

repeated_indices = []

for i in range(len(nums)):
    if nums.count(nums[i]) > 1 and i not in repeated_indices:
            repeated_indices.append(i)

tuple_repeated_indices = tuple(repeated_indices)

print(*tuple_repeated_indices)