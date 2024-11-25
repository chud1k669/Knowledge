def is_even(a):
    return a % 2 == 0

i = int (input ( ))
while i != 1:
    if is_even(i) == True:
        print(i)
    i = int (input ( ))
