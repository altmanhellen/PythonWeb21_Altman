
'''
Задача 5

Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите, может ли ферзь
попасть с первой клетки на вторую одним ходом.

'''

aFirst = int(input('Введите координату а первой клетки: '))
bFirst = int(input('Введите координату b первой клетки: '))
aSecond = int(input('Введите координату а второй клетки: '))
bSecond = int(input('Введите координату b второй клетки: '))

if aFirst == aSecond:
    print('YES')
elif bFirst == bSecond:
    print('YES')
elif aFirst + (aSecond - aFirst) == aSecond and bFirst - (aSecond - aFirst) == bSecond:
    print('YES')
elif aFirst + (aSecond - aFirst) == aSecond and bFirst + (aSecond - aFirst) == bSecond:
    print('YES')
elif aFirst - (aSecond - aFirst) == aSecond and bFirst - (aSecond - aFirst) == bSecond:
    print('YES')
elif aFirst - (aSecond - aFirst) == aSecond and bFirst + (aSecond - aFirst) == bSecond:
    print('YES')
else:
    print('NO')