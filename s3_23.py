"""
Задача №23. 
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3] 
Output: 2 (-1 < 5, 2 < 3) 
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""

import os

os.system('cls')

list = [0, -1, 5, 2, 3, 4, 12, 0, 34]

count = 0
count1=0
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        print(f'({list[i]}<{list[i+1]})')
        count += 1

print(f'Result: {count}')

res_list1 = [list[i+1] for i in range(len(list)-1) if list[i] < list[i+1]]
print(res_list1)
print(len(res_list1))
res_list2 = [list[i+1] if list[i] < list[i+1] else '*' for i in range(len(list)-1) ]
print(res_list2)
