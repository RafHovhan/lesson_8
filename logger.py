from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        b = []
        for i in data:
            data_list.append(i)
        data_list = [i.rstrip('\n') for i in data_list]
        data_list = list(filter(lambda x: x != '', data_list))
        for i in range(0, len(data_list), 4):
            b.append("\n".join(data_list[i:i+4]))
        g = '\n\n'.join(b)
        print(g)

    print('')
    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))

def delete_data():
    print('---В случае удаления контакта он навсегда удаляется с устройства---')
    b = int(input(f'Из какого варианта вы хотите удалить номер?\n'
                  f'1 - 1 Вариант\n'
                  f'2 - 2 Вариант\n'
                  f'Ваш выбор: '))
    a = input('Пожалуйста, укажите телефонный номер контакта, который вы хотите удалить: ')
    if b == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list()
            b = []
            d = []
            phnm = []
            for i in data:
                data_list.append(i)
            data_list = [i.rstrip('\n') for i in data_list]
            data_list = list(filter(lambda x: x != '', data_list))
            for i in range(2, len(data_list), 4):
                phnm.append(data_list[i])
            while a not in phnm:
                a = input("Такого телефонного номера не существует. Попробуйте снова: ")
            if a in phnm:
                for i in range(len(data_list)):
                    if data_list[i] == a:
                        b.append(i + 1)
                        b.append(i)
                        b.append(i - 1)
                        b.append(i - 2)
            b.sort(reverse = True)
            for i in b:
                del data_list[i]

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            for i in range(0, len(data_list), 4):
                d.append("\n".join(data_list[i:i+4]))
            g = '\n\n'.join(d)
            file.write(g)

    elif b == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            data = [i.rstrip('\n') for i in data]
            data = list(filter(lambda x: x != '', data))
            ph = []
            d = []
            for i in data:
                ph.append(i.split(';')[2])
            while a not in ph:
                a = input("Такого телефонного номера не существует. Попробуйте снова: ")
            f = 1
            for i in data:
                if f == 1:
                    if a in i:
                        data.remove(i)
                        f = 0
            print(data)

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            for i in data:
                g = '\n\n'.join(data)
            file.write(g)