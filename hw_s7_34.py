"""
Задача 34.
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод:
Парам пам-пам
"""
import os
os.system('cls')


def ritm(str):
    result_list = []
    lib = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    values = str.lower().split()
    for words in range(len(values)):
        count = 0
        for char in range(len(values[words])):
            if values[words][char] in lib:
                count += 1
        result_list.append(count)
    print(*list(zip(values, result_list)))
    if len(set(result_list)) == 1:
        return print('Парам пам-пам')
    return print('Пам парам')


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

ritm(str_1)
