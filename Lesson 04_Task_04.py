'''
Задача 4

Напишите программу, которая вычисляет значение выражения:  Формула

1 - A + Aˆ2 - Aˆ3 + ... + Aˆn

В первой строке содержатся вещественное число A (-3 < A < 3) и целое число n(1 <= n <= 20).
Вывести результат с точностью 0.001

'''

a = float(input('Введите первое число: '))
n = int(input('Введите второе число: '))
result = 0
s = 0

for x in range(0, n + 1):
    result = a ** x
    x += 1
    if x % 2 != 0:
        s += result
    else:
        s = s - result

print('%.3f' % s)