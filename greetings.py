# Определяем переменные


username = input ('Имя пользователя ')
title = input ('Заголовок заметки ')
content = input ('Описание заметки ')
status = input ('Статус заметки ')
from datetime import date
current_date = date.today()
created_date = print ('Дата создания заметки: ', current_date)
short_date = current_date.strftime ("%m.%d")
expiry_date = input ('Дата истечения заметки')

print ('Имя пользователя:', username)
print ('Заголовок заметки:', title)
print ('Описание заметки:', content)
print ('Статус заметки:', status)
print ('Дата создания заметки: ' , short_date)
print ('Дата истечения заметки:', expiry_date)







