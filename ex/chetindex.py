# lst_num = list(map(float, input().split()))
# lst_res = [v for i,v in enumerate(lst_num) if i % 2 == 0]
# print(lst_res)
(lst_num := list(map(float, input().split())), print(*[v for i,v in enumerate(lst_num) if i % 2 == 0]))
