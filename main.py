import time
from random import choice
from string import printable
all_characters = list(printable)
num = len(all_characters)
num_one = num - 5
all_characters = all_characters[:num_one]
status = False
while not status:
    length_pass = int(input('Введите длину пароля: '))
    if 7 <= length_pass <= 20:
        print('Длина пароля подходящая. Начинаем генерировать пароль...')
        time.sleep(2)
        status = True
    else:
        print('Длина пароля должна быть от 7 до 20 символов')
while status: 
    password = ''.join([choice(all_characters) for number in range(length_pass)])
    print(f'Сгенерированный пароль: {password}')
    us_answ = input('Нравится ли вам пароль? (да/нет) ').lower()
    if us_answ == 'нет':
        print('Давайте сгенерируем другой пароль...')
        time.sleep(2)
    elif us_answ == 'да':
        status = False
        print(f'Поздравляем! Ваш новый пароль: {password}')
    else:
        print('Остановка программы. Запрос не найден...')
        break
    





    