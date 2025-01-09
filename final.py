note={}
note['username'] = input("Введите имя пользователя: ")
note['content'] = input("Введите описание заметки: ")
note['status'] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note['created_date'] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note['issue_date'] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Создаем список заголовков заметки
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)


print("\nВы ввели следующие данные:")
print('Имя пользователя:', 'username')
print('Заголовок заметки:', 'title')
print('Описание заметки:', 'content')
print('Статус заметки:', 'status')
print('Дата создания заметки: ' , 'short_date')
print('Дата истечения заметки:', 'short_expiry_date')
print(titles)
print (note)
