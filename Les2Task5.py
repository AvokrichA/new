rating = [7, 5, 3, 3, 2]
user_rating = int(input('Оцените работу оператора от 1 до 10:'))
answer = False
for index, elem in enumerate(rating):
    if user_rating > elem:
        rating.insert(index, user_rating)
        answer = True
        break

if not answer:
    rating.append(user_rating)

print(rating)
