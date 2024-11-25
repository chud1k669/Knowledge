words = set(word.lower() for word in input().split())  
count = 0

if 'и' in words:
    count = sum(1 for word in words if word == 'и')

print(count)