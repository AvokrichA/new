name_user= (input('Введите ФИО полностью:')).split()
for a, b in enumerate(name_user):
    print(f'{a} - {b[:10]}')
    # testing