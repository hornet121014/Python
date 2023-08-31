import os
import random
os.system('cls')

N = input("Введите общее количество рассматриваемых монеток N>0: ")

count0 = count1 = 0

if N.isdigit() == True and int(N) > 0:
    N = int(N)
    list = [random.randrange(0, 2, 1) for i in range(N)]
    print(list)
    for i in range(len(list)):
        if list[i]==0:
            count0+=1
        elif list[i]==1:
            count1+=1
    print(min(count0,count1))

else:
    print("Ошибка ввода данных: введите натуральное положительное число N>0")
