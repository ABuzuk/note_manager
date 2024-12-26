# Определяем переменные


username = input ('Имя пользователя ')
title = input ('Заголовок заметки ')
content = input ('Описание заметки ')
status = input ('Статус заметки ')
from datetime import date
current_date = date.today()
created_date = print ('Дата создания заметки: ',current_date)
short_date = current_date.strftime ("%m.%d")
expiry_date = input ('Дата истечения заметки в формате гггг.мм.дд: ')
short_expiry_date = expiry_date [6:11]

print ('Имя пользователя:', username)
print ('Заголовок заметки:', title)
print ('Описание заметки:', content)
print ('Статус заметки:', status)
print ('Дата создания заметки: ' , short_date)
print ('Дата истечения заметки:', short_expiry_date)






