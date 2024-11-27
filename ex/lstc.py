str_city = input()
cities_list = str_city.split()
(*lst_c,) = cities_list
print(lst_c)
#lst_c = *input().split(),
#print(lst_c)