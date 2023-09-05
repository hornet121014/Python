import os
os.system('cls')

n = input("Введите число n: ")
k=0
if n.isdigit() == True and int(n) > 0:
    n = int(n)
    while 2**k<n:
        print(f"{2**k}", end=' ')
        k+=1
else:
    print("Ошибка ввода данных: введите целое число N>0")
