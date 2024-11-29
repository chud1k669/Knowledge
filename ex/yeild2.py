def balak_seq(max_len):
    a, b, c = 1, 1, 1
    count = 0
    
    while count < max_len:
        if count < 3:
            yield 1
        else:
            next_num = a + b + c
            yield next_num
            
            a, b, c = b, c, next_num
        
        count += 1

N = int(input())

sequence = [str(num) for num in balak_seq(N)]
print(" ".join(sequence))