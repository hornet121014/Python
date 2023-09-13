import os
import random

os.system('cls')

list1=[random.randint(0,10) for _ in range(10)]
#list1=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
print(list1)

print('Введите данные диапазона поиска:')
num1 = int(input('- введите начало: '))
num2 = int(input('- введите окончание: '))

list2=[_ for _ in range(num1,num2+1)]
list3=[]
#print(list2)

for i in range(len(list1)):
    if list1[i] in list2:
        list3.append(i)

print(list3)
