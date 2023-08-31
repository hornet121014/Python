import os
os.system('cls')

s,p = input("Введите сумму чисел s: "),input("Введите произведение чисел p: ")
rangeX=rangeY=1001

if s.isdigit() == True and p.isdigit() == True and int(s) > 1 and int(p) > 1:
    s,p = int(s), int(p)
    for x in range(rangeX):
        for y in range(rangeY):
            if x+y==s and x*y==p:
                print(f"x={x} y={y}")
else:
    print("Ошибка ввода данных: введите натуральные положительные числа >0")