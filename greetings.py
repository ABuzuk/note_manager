# Определяем переменные

username = input ('Введите имя пользователя ')
title = input ('Введите заголовок заметки ')
content = input ('Введите описание заметки ')
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
from datetime import date
current_date = date.today()
created_date = print ('Дата создания заметки: ',current_date)
short_date = current_date.strftime ("%m.%d")
expiry_date = input ('Дата истечения заметки в формате гггг.мм.дд: ')
short_expiry_date = expiry_date [6:11]

# Создаем список заголовков заметки
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)


print("\nВы ввели следующие данные:")
print ('Имя пользователя:', username)
print ('Заголовок заметки:', title)
print ('Описание заметки:', content)
print ('Статус заметки:', status)
print ('Дата создания заметки: ' , short_date)
print ('Дата истечения заметки:', short_expiry_date)
print (titles)





