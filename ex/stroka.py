a,b = map(str, input().split())
word1 = a[:-(len(a)-len(b))]
print(word1[0::2]== b[0::2])