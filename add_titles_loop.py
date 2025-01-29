#инидциализация перемененой
titles = []
#делаем бесконечный цикл
for j in range (100):
    print
    title = input('Введите заголовок (или введите stop  для завершения): ')
    #вводим условие, при котором команда остановится
    if title == 'stop':
        break
    else:
        titles.append(title)
print(titles)
