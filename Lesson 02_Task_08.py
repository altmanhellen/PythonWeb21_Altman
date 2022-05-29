'''
Задача 8*

Есть две коробки, первая размером A1×B1×C1, вторая размером A2×B2×C2.
Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
что поворачивать коробки можно только на 90 градусов вокруг ребер.

Формат входных данных

Программа получает на вход числа A1, B1, C1, A2, B2, C2.

Формат выходных данных

Программа должна вывести одну из следующих строчек: Boxes are equal,
если коробки одинаковые, The first box is smaller than the second one,
если первая коробка может быть положена во вторую,
The first box is larger than the second one, если вторая коробка может быть положена в первую,
Boxes are incomparable, во всех остальных случаях.'

'''
a = int(input('Введите сторону a первой коробки: '))
b = int(input('Введите сторону b первой коробки: '))
c = int(input('Введите сторону c первой коробки: '))

d = int(input('Введите сторону a второй коробки: '))
e = int(input('Введите сторону b второй коробки: '))
f = int(input('Введите сторону c второй коробки: '))

if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if d > f:
    d, f = f, d
if e > f:
    e, f = f, e
if d > e:
    d, e = e, d
if a == d and b == e and c == f:
    print('Boxes are equal')
elif a <= d and b <= e and c <= f:
    print('The first box is smaller than the second one')
elif a >= d and b >= e and c >= f:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')