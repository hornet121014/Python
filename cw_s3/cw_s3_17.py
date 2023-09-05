"""
Задача №17. 
Дан список чисел. 
Определите, сколько в нем встречается различных чисел. 
Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6 
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""

import os
os.system('cls')

list=[1, 1, 2, 0, -1, 3, 4, 4]

#n=int(input('Enter n:'))
#for i in range(n):
#    list.append(int(input('Enter element:')))

my_set=set(list)

print(f'Set: {my_set}')

print(f'Result: {len(my_set)}')
