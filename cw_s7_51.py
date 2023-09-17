"""
Задача 51.
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод: 
values = [0, 2, 10, 6] #same
if same_by(lambda x: x % 2, values):
print('same')
else:
print('different')

Вывод:

"""
import os
os.system('cls')

def same_by(characteristic, objects):
    set_1=set(map(characteristic,objects))
    if len(set_1)==2:
        return False
    return True

values = [0, 2, 10, 6]
#values = [1, 3, 11, 8]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')