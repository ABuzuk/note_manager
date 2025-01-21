#инициализация переменной
titles = []
#запускаем возможность бесконечного добавления заголовков
while True:
    title1 = input('Введите заголовок (или введите stop для завершения): Основные идеи ')
    #проверяем на "стоп"
    if title1 == 'stop':
        break
    title2 = input("Введите заголовок (или введите stop для завершения): Список задач ")
    if title2 == 'stop':
        break
    title3 = input("Введите заголовок (или введите stop для завершения): ")
    if title3 == 'stop':
        break
    titles.append([title1, title2, title3])

print(titles)


#вариант 2

# while True:
#  titles = []
#     title = input('Введите заголовок (или введите stop  для завершения): Основные идеи ')
#     title = input("Введите заголовок (или введите stop для завершения): Список задач ")
#     title = input("Введите заголовок (или введите stop для завершения): ")
#     if title == 'stop':
#         break
#     else:
#         titles.append(title)
#
# print(titles)

#вариант 3
# titles = []
# for j in range (1, 100):
#     print
#     title1 = input('Введите заголовок (или введите stop  для завершения): Основные идеи ')
#         if title1 == 'stop':
#             break
#         else:
#             titles.append(title)
#     title = input("Введите заголовок (или введите stop для завершения): Список задач ")
#     title = input("Введите заголовок (или введите stop для завершения): ")
