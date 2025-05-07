# Импорты
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Устанавливаем путь выполнения кода

# Функция:
def reverseName(word): 
    result = word[::-1]
    return result

def create_directory(directory_path):
    try:
        # Создаем директорию, если она не существует
        os.makedirs(directory_path, exist_ok=True)
        print(f"Директория '{directory_path}' успешно создана.")
    except Exception as e:
        print(f"\033[31mОшибка при создании директории: {e}") 

# Эта программа принтер 2.0!

print('Вас приветствует Принтер 2.0, введите имя.')
name = input() 
print('Здравствуйте господин', name)

# Невероятно важный функционал
if name == "Ellis":
    print('Здравствуйте хозяин')

elif name == "Fanat":
    print('Здравствуйте великий создатель')

elif name == "DLTima":
    print('Вам вход запрещён. Уходите. Это приказ. пожалуйста...')

elif name == "член":
    print('Я же сказал, члены не добавим! (навреное)')

else:
    print(f'Добро пожаловать, {name}.') 

 
# цикл
# for i in range(10):
#     print(name)

# Тест Функции
print(reverseName(name))
