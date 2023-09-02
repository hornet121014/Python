"""
Задача 20.
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так: 
● A, E, I, O, U, L, N, S, T, R – 1 очко; 
● D, G – 2 очка; 
● B, C, M, P – 3 очка; 
● F, H, V, W, Y – 4 очка; 
● K – 5 очков; 
● J, X – 8 очков; 
● Q, Z – 10 очков. 

А русские буквы оцениваются так: 
● А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
● Д, К, Л, М, П, У – 2 очка; 
● Б, Г, Ё, Ь, Я – 3 очка; 
● Й, Ы – 4 очка; 
● Ж, З, Х, Ц, Ч – 5 очков; 
● Ш, Э, Ю – 8 очков; 
● Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Ввод: ноутбук 
Вывод: 12
"""

import os
os.system('cls')

def isEnglish(letter):   # состоит ли строка из английских букв
    return letter.isascii() and letter.isalpha()

def isRussian(letter):   # состоит ли строка из английских букв
    flag=False
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 
    cyrillic_upper_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' 
    cyrillic_letters = cyrillic_lower_letters + cyrillic_upper_letters 
    for i in range(len(letter)):
        if letter[i] in cyrillic_letters:
            flag=True
        else:
            flag=False
            break
    return flag and letter.isalpha()

def Scrabble(str,lib):
    count=0
    for cur_lib in lib:
        for key in cur_lib:
            for i in str:
                if i in cur_lib[key]:
                    count+=key
    print(f'Стоимость слова составляет: {count}')

k=input('Введите слово: ')
k=k.upper()

library_eng={1:'AEIOULNSTR'},{2:'DG'},{3:'BCMP'},{4:'FHVWY'},{5:'K'},{8:'JX'},{10:'QZ'}
library_rus={1:'АВЕИНОРСТ'},{2:'ДКЛМПУ'},{3:'БГЁЬЯ'},{4:'ЙЫ'},{5:'ЖЗХЦЧ'},{8:'ШЭЮ'},{10:'ФЩЪ'}

if isEnglish(k):
    Scrabble(k,library_eng)
elif isRussian(k):
    Scrabble(k,library_rus)
else:
    print('Введите корректное слово')