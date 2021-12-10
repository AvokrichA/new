list1 = input("Перечислите не менее 5 наименований:").split()
your_list = len(list1)
i=0
if your_list > 1:
    while i < your_list - 1:
        your_list[i], your_list[i+ 1] = your_list[i + 1], your_list[i]
        i += 2

print(your_list)
# testing