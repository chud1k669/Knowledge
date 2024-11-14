fio = list(map(str, input().split()))
name = fio[0]
otch = fio[1]
print(fio[2]+' ',*name[0]+'.', *otch[0]+'.', sep="")