import os
os.system('cls')

def progressia(a,b,c):
    an=a+(c-1)*b
    return [i for i in range(a,an+1,b)]

print('Введите данные арифметической прогрессии:')
num1 = int(input('- введите первый элемент: '))
step = int(input('- введите шаг: '))
count = int(input('- введите количество элементов: '))

mylist=progressia(num1,step,count)

print(*mylist)