'''
Задача 3

Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
Даны две различные клетки шахматной доски, определите, может ли король попасть
с первой клетки на вторую одним ходом.

Формат входных данных

Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
сначала для первой клетки, потом для второй клетки.

Формат выходных данных

Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.

'''

aFirst = int(input('Введите координату а первой клетки: '))
bFirst = int(input('Введите координату b первой клетки: '))
aSecond = int(input('Введите координату а второй клетки: '))
bSecond = int(input('Введите координату b второй клетки: '))

if aFirst == aSecond:
    print('YES')
elif bFirst == bSecond:
    print('YES')
elif aFirst + 1 == aSecond and bFirst - 1 == bSecond:
    print('YES')
elif aFirst + 1 == aSecond and bFirst + 1 == bSecond:
    print('YES')
elif aFirst - 1 == aSecond and bFirst - 1 == bSecond:
    print('YES')
elif aFirst - 1 == aSecond and bFirst + 1 == bSecond:
    print('YES')
else:
    print('NO')