import os
os.system('cls')

def fillset(a):
    myset=set([int(input(f'{i+1}: ')) for i in range(a)])
    return myset

n = int(input('Введите n: '))
m = int(input('Введите m: '))
print('Введите элементы множества n:')
myset1=fillset(n)
print('Введите элементы множества m:')
myset2=fillset(m)
mylist=sorted(list(myset1 & myset2))
print(f'Числа, которые встречаются в обоих множествах: {mylist}')
