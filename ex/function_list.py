lst = list(map(int, input().split()))
min_num = 0
max_num = 0
sum_nums = 0
def get_min_max_sum(min_num, max_num, sum_nums, lst):
    min_num = min(lst)
    max_num = max(lst)
    sum_nums = sum(lst)
    print(f'Min = {min_num}, max = {max_num}, sum = {sum_nums}')

get_min_max_sum(min_num, max_num, sum_nums, lst)
