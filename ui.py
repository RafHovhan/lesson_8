from logger import input_data, print_data, delete_data

def interface():
    print('Добрый день! Это бот-помощник.\n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Удалить контакт')
    
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка! Попробуйт ещё раз! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()