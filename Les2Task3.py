month=input("Введите число месяца от 1 до 12:")
win = 'зима'
spr = 'весна'
sum = 'лето'
aut = 'осень'
dict_season= {'1':win , '2':win, '3':spr, '4':spr, '5':spr, '6':sum, '7':sum, '8':sum, '9':aut, '10':aut, '11':aut, '12':win}
print(dict_season[month])

month_list=[win, win, spr, spr, spr, sum, sum, sum, aut, aut, aut, win,win]
print(month_list[int(month)])
# testing