def setXstrTOint(x,str):
    list=str.split()
    list=list[:x]
    myset=set([int(item) for item in list])
    return myset

n = int(input('Введите n: '))
m = int(input('Введите m: '))
sn=input(f'Введите {n} элемента(ов) множества n одной строкой: ')
sm=input(f'Введите {m} элемента(ов) множества m одной строкой: ')
myset1=setXstrTOint(n,sn)
myset2=setXstrTOint(n,sm)
myset=myset1&myset2
print(*sorted(list(myset)))
