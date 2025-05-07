# Функция:
def reverseName(word): 
    result = word[::-1]
    return result 

# Эта программа принтер 2.0!

print('Вас приветствует Принтер 2.0, введите имя.')
name = input() 
print('Здравствуйте господин', name)

# Невероятно важный функционал
if name == "Ellis":
    print('Здравствуйте хозяин')

if name == "Fanat":
    print('Здравствуйте великий создатель')

if name == "DLTima":
    print('Вам вход запрещён. Уходите. Это приказ. пожалуйста...')

# цикл
# for i in range(10):
#     print(name)

# Тест Функции
print(reverseName(name))

