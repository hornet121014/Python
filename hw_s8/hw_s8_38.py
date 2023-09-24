"""
Задача №49.
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
4. Использование функций. 
Ваша программа не должна быть линейной
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


def interface():
    cmd = '0'
    while cmd != '4':
        print('Выбирете действие:\n'
              '1. добавить контакт\n'
              '2. вывести все контакты\n'
              '3. поиск контакта\n'
              '4. Выход\n'
              )
        cmd = input('→:')
        while cmd not in ('1', '2', '3', '4'):
            print('Некорректный ввод.')
            cmd = input('→:')
        match cmd:
            case '1': enter_data()
            case '2': print_data()
            case '3': search_data()
            case '4': print('Всего доброго.')


interface()
