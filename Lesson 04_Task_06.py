'''
Задача 6

В первой строке содержится целое число n (1 <= n <= 100). - количество членов ряда.
Вывести сумму членов ряда с точностью 0.000001.

'''

k = 1
n = int(input('Введите целое число от 1 до 100: '))
a = 2
s = 1
num = 0
result = 0

for x in range(k, n + 1):
    s *= x
    result += 1 / a
    a += 1
    num += s / result

print('%.6f' % num)