words = set(word.lower() for word in input().split())  
s = set()

for i in words:
    if len(i) >= 3:  
        s.add(i)

print(len(s)) 