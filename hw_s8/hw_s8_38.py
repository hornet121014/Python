"""
Задача №38.
Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
"""

import os
os.system('cls')


def enter_first_name():
    return input('Введите имя: ').title()


def enter_second_name():
    return input('Введите фамилию: ').title()


def enter_family_name():
    return input('Введите отчество: ').title()


def enter_phone_number():
    return input('Введите номер телефона: ')


def enter_adress_user():
    return input('Введите адрес: ')


def enter_data():
    i_name = enter_first_name()
    f_name = enter_second_name()
    o_name = enter_family_name()
    num_phone = enter_phone_number()
    adress = enter_adress_user()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{f_name} {i_name} {o_name}\n{num_phone}\n{adress}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read())
        print()


def search_data():
    print('Выбирете вариант поиска:\n'
          '1. Фамилия\n'
          '2. Имя\n'
          '3. Отчество\n'
          '4. Номер телефона\n'
          '5. Адрес\n')
    index = int(input('→ : '))-1
    line = input('Введите строку поиска: ').title()
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if line in new_item[index]:
                print()
                print(item)
                print()


def edit_data():
    print('Выбирете вариант изменения:\n'
          '1. Фамилия\n'
          '2. Имя\n'
          '3. Отчество\n'
          '4. Номер телефона\n'
          '5. Адрес\n'
          )
    index = int(input('→ : '))-1
    find_str = input('Введите строку поиска: ').title()
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if find_str in item:
                k = data.index(item)
                new_data = input('Введите новые данные: ').title()
                new_item[index] = new_data
                data[k] = f'{new_item[0]} {new_item[1]} {new_item[2]}\n{new_item[3]}\n{new_item[4]}'.strip(
                )
                with open('phonebook.txt', 'w', encoding='UTF-8') as file:
                    file.write('\n\n'.join(data))
                print('Данные успешно изменены')


def delete_data():
    print('Выбирете вариант удаления:\n'
          '1. Фамилия\n'
          '2. Имя\n'
          '3. Отчество\n'
          '4. Номер телефона\n'
          '5. Адрес\n'
          )
    index = int(input('→ : '))-1
    find_str = input('Введите строку поиска: ').title()
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if find_str in item:
                k = data.index(item)
                data.pop(k)
                with open('phonebook.txt', 'w', encoding='UTF-8') as file:
                    file.write('\n\n'.join(data)+'\n\n')
                print('Данные успешно удалены\n')


def interface():
    cmd = '0'
    while cmd != '6':
        print('Выбирете действие:\n'
              '1. добавить контакт\n'
              '2. вывести все контакты\n'
              '3. поиск контакта\n'
              '4. изменить контакт\n'
              '5. удалить контакт\n'
              '6. Выход\n'
              )
        cmd = input('→:')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод.')
            cmd = input('→:')
        match cmd:
            case '1': enter_data()
            case '2': print_data()
            case '3': search_data()
            case '4': edit_data()
            case '5': delete_data()
            case '6': print('Всего доброго.')


interface()
