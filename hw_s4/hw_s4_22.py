def fillset(a,name):
    myset=set([int(input(f'Введите {i+1} элемент множества {name}: ')) for i in range(a)])
    return myset

n = int(input('Введите n: '))
m = int(input('Введите m: '))
myset1=fillset(n, 'n')
myset2=fillset(m, 'm')
mylist=sorted(list(myset1&myset2))
print(*mylist)
