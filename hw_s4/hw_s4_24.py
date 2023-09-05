"""
Задача №24. 
В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. 
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним. 
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.

4 -> 1 2 3 4 
9

5 → 9 1 2 3 8
20
"""
import os
os.system('cls')

sum=0
list=[]
result=[]

n = int(input('Введите количество кустов: '))

print(f'Введите урожайность кустов: ')
for i in range(n):
    list.append(int(input(f'{i+1}: ')))

for i in range(n):
    if i==n-1:
        sum=list[i-1]+list[i]+list[i-n+1]
        result.append(sum)
    else:
        sum=list[i-1]+list[i]+list[i+1]
        result.append(sum)

print(f'Максимальное число ягод, которое можно собрать за один заход, составляет {max(result)}')
