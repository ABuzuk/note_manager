#импортируем модуль даты из библиотеки
from datetime import datetime
#задаем текущую дату
current_date = datetime.now()
print("Текущая дата:", current_date.strftime('%d/%m/%Y'))

#проверяем на дедлайны
while True:
    try:
        # вводим дедлайн
        deadline = input("Введите дату дедлайна (в формате день/месяц/год): ")
        issue_date = datetime.strptime(deadline, "%d/%m/%Y")

        # Вычисляем разницу во времени
        time_difference = issue_date - current_date
        days_difference = time_difference.days
        
        #проверяем статус дедлайна и выводим сообщение
        if days_difference > 0:
            print("До Дедлайна осталось", days_difference, "дней.")
        elif days_difference < 0:
            print ("Дедлайн истек", days_difference, "дней назад.")
        elif days_difference == 0:
            print ("Дедлайн сегодня!")
        break
        #отрабатываем ошибку ввода
    except ValueError:
        print("Неверный ввод! Пожалуйста, введите дату в формате ДД/ММ/ГГГГ.")
