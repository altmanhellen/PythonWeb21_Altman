'''
Задача 5.
Дано натуральное n. Вычислить сумму членов ряда по формуле:


В первой строке содержится целое число n (1 <= n <= 100). - количество членов ряда.
Вывести сумму членов ряда с точностью 0.000001.

'''

k = 1
n = int(input())
s = 0
result = 0


for x in range(k, n + 1):
    result += 1 / ((2 * x) ** 2)
    s += x

print('%.6f'% result)