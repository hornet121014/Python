"""
Задача №18. 
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""

import os
os.system('cls')

list_1=[1, 2, 3, 4, 5,10]

k=8

res=[abs(list_1[i]-k) for i in range(len(list_1))]


x=res.index(min(res))

print(list_1[x])