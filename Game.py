import time  # Импортируем модуль time для работы со временем

time.sleep(1)

print('Здравствуйте, представтесь.')
name = input()

time.sleep(1)

print(f'Добро пожаловать, {name}.\nМы рады приветствовать вас в нашей игре!\n')
time.sleep(1)

print('Смысл игры состоит в том что мы задаём вопросы, вы отвечаете.\nСыграем?')
time.sleep(1)

# Начинаем бесконечный цикл
while True:

    # Запрашиваем у пользователя ввод
    user_input = input("Да/Нет: ").strip()  # Удаляем лишние пробелы

    # Проверяем, соответствует ли введенное значение 'Да'
    if user_input.lower() == 'да':
        time.sleep(1)
        print("Хорошо\n")  # Ответ для 'Да'

        break  # Выходим из цикла, так как пользователь ввел правильный ответ

    # Проверяем, соответствует ли введенное значение 'Нет'
    elif user_input.lower() == 'нет':
        time.sleep(1)
        print("Нет иди нахуй\n")  # Ответ для 'Нет'

        break  # Выходим из цикла

    else:
        print(f"{name}, ты тупой? Тебе сказано пиши Да или нет, так вот пиши да или нет.'.\n")  # Сообщаем об ошибке и продолжаем цикл

time.sleep(2)

# НАЧАЛО ИГРЫ
# Объяснение правил игры:
print('\nЧто-ж. Начнём с простого. Правила игры:\n1. Вам будет задано к примеру 10 вопросов. Вам надо будет ответить на каждый верно. Вопросы имеют разный харатер.')
time.sleep(1)
print('2. Если вы вводите что-либо кроме ответа, вы переноситесь в начало. И будет так до тех пор пока тест не будет пройден.\n')
time.sleep(3)
print('Начнём.\n')


        # ВОПРОСЫ В СТУДИЮ:
time.sleep(1)
print('1 из 8 вопрос.\n')
time.sleep(1)

while True: # Начинаем бесконечный цикл
    time.sleep(1)
    user_input = input('Из какой части готики маг: Карристо?\nВарианты ответа:\n1 2 3\nВаш ответ: ')

    if user_input.lower() == '1':
        time.sleep(1)
        print('Молодец, верно. Карристо это верховный маг круга огня из первой готики.')

        break  # Выходим из цикла, так как пользователь ввел правильный ответ
    else:
        time.sleep(1)
        print('Неверно.\n') 

#ВОПРОС 2

time.sleep(1)
print('2 из 8 вопрос.\n')
time.sleep(1)   

while True: # Начинаем бесконечный цикл
    time.sleep(1)
    user_inpu = input('Что можно сделать с амулетом из Hollow Knight: Хрупкая сила. Варианты ответа:\n1. Сломать, починить, улучшить за 15к гео.\n2.Сломать.\n Починить, сломать, продать.\n')
    if user_input.lower() == '1':
        time.sleep(1)
        print('Верно. После призыва шайки гримма в Грязьмут, можно зайти в левую палатку и отдать амулет женщине, она его съест, чтобы вернуть его надо заплатить 15к гео, тогда он станет нерушимым.\n Он ломается при базовой версии\nЕго можно починить у торговца этими амулетами за доп гео.')

        break  # Выходим из цикла, так как пользователь ввел правильный ответ
    else:
        time.sleep(1)
        print('Неверно.\n') 